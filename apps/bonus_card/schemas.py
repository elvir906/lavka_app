from pydantic import BaseModel
from typing import Optional


class BonusCardBase(BaseModel):
    code: Optional[str] = None


class BonusCardCreate(BonusCardBase):
    user_id: int


class BonusCardUpdate(BonusCardBase):
    pass


class BonusCardDB(BaseModel):
    id: int

    class Config:
        orm_mode = True


# По этой схеме данные отправляются клиенту
class BonusCard(BonusCardDB):
    code: Optional[str] = None
    user_id: Optional[int] = None


class BonusCardInDB(BonusCardDB):
    pass
