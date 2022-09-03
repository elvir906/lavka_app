from typing import Any, Dict, List, Optional, Union
from sqlalchemy.orm import Session

from apps.base.crud import BaseCRUD
from .models import PromoAction as ModelPromoAction
from .schemas import PromoActionCreate, PromoActionUpdate


class PromoActionCRUD(BaseCRUD[
    ModelPromoAction, PromoActionCreate, PromoActionUpdate
]):
    def get_by_id(self, db: Session, *, id: str) -> Optional[ModelPromoAction]:
        return db.query(ModelPromoAction).get(id)

    def get_multi_with_sort(self, db: Session) -> List[ModelPromoAction]:
        return db.query(ModelPromoAction).order_by(ModelPromoAction.sort).all()

    def create(
        self, db: Session, *, obj_in: PromoActionCreate
    ) -> ModelPromoAction:
        db_obj = ModelPromoAction(
            is_active=obj_in.is_active,
            title=obj_in.title,
            type=obj_in.type,
            iconpath=obj_in.iconpath,
            imagepath=obj_in.imagepath,
            subtitle=obj_in.subtitle,
            attention_text=obj_in.attention_text,
            description=obj_in.description,
            sort=obj_in.sort
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelPromoAction,
        obj_in: Union[PromoActionUpdate, Dict[str, Any]]
    ) -> ModelPromoAction:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def is_active(self, Promoution: ModelPromoAction) -> bool:
        return Promoution.is_active

    def delete(self, db: Session, *, id: str) -> Optional[ModelPromoAction]:
        db_obj = db.query(ModelPromoAction).get(id)
        db.delete(db_obj)
        db.commit()
        return db_obj


promoaction_crud = PromoActionCRUD(ModelPromoAction)
