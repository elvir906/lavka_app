from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from core.utils import get_current_active_superuser, get_db
from apps.user.models import User as ModelUser
from apps.user.schemas import User, UserCreate, UserDelete, UserUpdate
from apps.user.crud import crud_user


router = APIRouter()


@router.get('/get_user_by_id/', response_model=User)
def read_user_id(
    db: Session = Depends(get_db),
    user_id: int = 0,
    current_user: ModelUser = Depends(get_current_active_superuser)
):
    if current_user.is_superuser:
        return crud_user.get_by_id(db, id=user_id)


@router.get('/get_all_users/', response_model=List[User])
def read_users_page_sizepage(
    db: Session = Depends(get_db),
    page: int = 0,
    page_size: int = 10,
    current_user: ModelUser = Depends(get_current_active_superuser)
):
    if current_user.is_superuser:
        users = crud_user.get_multi(db, page=page, page_size=page_size)
        return users


@router.post('/create_user/', response_model=User)
def create_user(
    *,
    db: Session = Depends(get_db),
    user_in: UserCreate,
    current_user: ModelUser = Depends(get_current_active_superuser)
):
    user = crud_user.get_by_phone(db, phone=user_in.phone)
    if user:
        raise HTTPException(
            status_code=400,
            detail='Пользователь с таким номером телефона уже существует.',
        )
    if current_user.is_superuser:
        user = crud_user.create(db, obj_in=user_in)
        return user


@router.delete('/delete_user/', response_model=User)
def delete_user(
    *,
    db: Session = Depends(get_db),
    user_in: UserDelete,
    current_user: ModelUser = Depends(get_current_active_superuser)
) -> User:
    user = crud_user.get_by_id(db, id=user_in.id)
    data = {'id': user_in.id,
            'name': 'deleted',
            'family': None,
            'patronymic': None,
            'phone': '0',
            'is_superuser': False,
            'is_active': False}
    if current_user.id == user_in.id or current_user.is_superuser:
        user = crud_user.del_update(db, db_obj=user, obj_in=data)
        return user


@router.put('/update_user/', response_model=User)
def update_user(
    *,
    db: Session = Depends(get_db),
    user_in: UserUpdate,
    current_user: ModelUser = Depends(get_current_active_superuser)
) -> User:
    user = crud_user.get_by_id(db, id=user_in.id)

    if current_user.id == user_in.id or current_user.is_superuser:
        user = crud_user.del_update(db, db_obj=user, obj_in=user_in)
        return user
