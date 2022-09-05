from typing import Optional

from pydantic import BaseModel


class PromoActionBase(BaseModel):
    title: Optional[str] = None
    type: Optional[str] = None
    iconpath: Optional[str] = None
    imagepath: Optional[str] = None
    subtitle: Optional[str] = None
    attention_text: Optional[str] = None
    description: Optional[str] = None
    sort: Optional[int] = None
    is_active: Optional[bool] = False


class PromoActionCreate(PromoActionBase):
    pass


class PromoActionUpdate(PromoActionBase):
    pass


class PromoActionDB(BaseModel):
    id: int

    class Config:
        orm_mode = True


# По этой схеме данные отправляются клиенту
class PromoAction(PromoActionDB):
    title: str
    type: str
    iconpath: str


class PromoActionInDB(PromoActionDB):
    pass
