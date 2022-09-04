from fastapi.encoders import jsonable_encoder
from typing import List, Optional
from sqlalchemy.orm import Session

from core.security import verify_password, get_password_hash
from apps.base.crud import BaseCRUD
from .models import User
from .schemas import UserCreate, UserDB, UserDelete, UserUpdate


class UserCRUD(BaseCRUD[User, UserCreate, UserUpdate]):
    def get_by_id(self, db: Session, *, id: int) -> Optional[User]:
        return db.query(User).get(id)

    def get_by_phone(self, db: Session, *, phone: str) -> Optional[User]:
        return db.query(User).filter(User.phone == phone).first()

    def get_by_name(self, db: Session, *, name: str) -> Optional[User]:
        return db.query(User).filter(User.name == name).first()

    def get_multi(
        self, db: Session, *, page: int = 0, page_size: int = 10
    ) -> List[User]:
        return db.query(User).offset(page*page_size).limit(page_size).all()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            name=obj_in.name,
            family=obj_in.family,
            patronymic=obj_in.patronymic,
            phone=obj_in.phone,
            hashed_password=get_password_hash(obj_in.password),
            is_superuser=obj_in.is_superuser,
            is_active=True,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: User,
        obj_in: UserUpdate
    ) -> User:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def del_update(
        self,
        db: Session,
        *,
        db_obj: User,
        obj_in: UserDelete
    ) -> User:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def authenticate(
        self, db: Session, *, name: str, password: str
    ) -> Optional[User]:
        user = self.get_by_name(db, name=name)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


crud_user = UserCRUD(User)
