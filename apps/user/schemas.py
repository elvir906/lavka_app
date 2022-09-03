from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    name: Optional[str] = None
    family: Optional[str] = None
    patronymic: Optional[str] = None


class UserCreate(UserBase):
    phone: str
    password: str
    is_superuser: bool = False


class UserUpdate(UserBase):
    id: int
    phone: str
    password: str


class UserDelete(BaseModel):
    id: int


class UserDB(BaseModel):
    id: int

    class Config:
        orm_mode = True


# По этой схеме отправляются клиенту
class User(UserDB):
    name: Optional[str] = None
    family: Optional[str] = None
    patronymic: Optional[str] = None
    phone: str


class UserInDB(UserDB):
    pass
