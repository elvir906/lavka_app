from typing import Any, Dict, List, Optional, Union
from sqlalchemy.orm import Session

from apps.base.crud import BaseCRUD
from .models import BonusCard
from .schemas import BonusCardCreate, BonusCardUpdate


class BonusCardCRUD(
    BaseCRUD[
        BonusCard,
        BonusCardCreate,
        BonusCardUpdate
    ]
):
    def get_by_id(self, db: Session, *, id: int) -> Optional[BonusCard]:
        return db.query(BonusCard).get(id)

    def get_by_code(self, db: Session, *, code: str) -> Optional[BonusCard]:
        return db.query(BonusCard).filter(BonusCard.code == code).first()

    def get_by_user_id(
        self,
        db: Session,
        *,
        user_id: int
    ) -> Optional[BonusCard]:
        return db.query(BonusCard).filter(BonusCard.user_id == user_id).first()

    def get_all(
        self,
        db: Session,
        *,
        page: int = 0,
        page_size: int = 10
    ) -> List[BonusCard]:
        return db.query(
            BonusCard
        ).offset(page*page_size).limit(page_size).all()

    def create(self, db: Session, *, obj_in: BonusCardCreate) -> BonusCard:
        db_obj = BonusCard(
            code=obj_in.code,
            user_id=obj_in.user_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: BonusCard,
        obj_in: Union[BonusCardUpdate, Dict[str, Any]]
    ) -> BonusCard:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def delete(self, db: Session, *, id: int) -> Optional[BonusCard]:
        db_obj = db.query(BonusCard).get(id)
        db.delete(db_obj)
        db.commit()
        return db_obj


crud_bonus_card = BonusCardCRUD(BonusCard)
