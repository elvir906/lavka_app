from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from core.settings import Settings
from core.security import create_token
from apps.base.schemas import Token
from apps.user.crud import crud_user
from core.utils import get_db


router = APIRouter()


@router.post('/login/access-token', response_model=Token, tags=['auth'])
def login_access_token(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user = crud_user.authenticate(
        db, name=form_data.username, password=form_data.password)

    if not user:
        raise HTTPException(
            status_code=400, detail='Неверный пользователь и/или пароль')
    elif not crud_user.is_active(user):
        raise HTTPException(status_code=400, detail='Неактивный пользователь')
    access_token_expires = timedelta(
        minutes=Settings.ACCESS_TOKEN_VALIDITY_MINUTES)
    return {
        'access_token': create_token(
            data={'user_id': user.id}, expires_delta=access_token_expires
        ),
        'token_type': 'bearer',
    }
