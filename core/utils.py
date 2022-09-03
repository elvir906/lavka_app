from starlette.requests import Request
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from random import randint

from apps.base.schemas import TokenPayload
from apps.user.models import User
from apps.user.crud import crud_user
from . security import ALGORITHM
from . settings import EnvData


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl='auth/login/access-token/'
)
password_reset_jwt_subject = 'preset'


def get_db(request: Request):
    return request.state.db


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> User:
    try:
        payload = jwt.decode(
            token, EnvData.secret, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Не удалось валидировать данные',
        )
    user = crud_user.get(db, id=token_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    return user


def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    if not crud_user.is_active(current_user):
        raise HTTPException(status_code=400, detail='Неактивный пользователь')
    return current_user


def get_current_active_superuser(
    current_user: User = Depends(get_current_user),
) -> User:
    if not crud_user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail='Пользователь не имеет достаточных прав'
        )
    return current_user


def create_unique_card_code(code_lenght):
    range_start = 10**(code_lenght-1)
    range_end = (10**code_lenght)-1
    return str(randint(range_start, range_end))
