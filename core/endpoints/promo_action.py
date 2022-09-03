from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.utils import (
    get_db,
    get_current_active_superuser
)
from apps.promo_action.crud import promoaction_crud
from apps.promo_action.schemas import (
    PromoActionCreate,
    PromoAction,
    PromoActionUpdate
)
from apps.user.models import User as UserModel


router = APIRouter()


@router.get('/get_promoactions/', response_model=List[PromoAction])
def read_promo(
    db: Session = Depends(get_db),
):
    return promoaction_crud.get_multi_with_sort(db)


@router.post('/create_promoaction/', response_model=PromoAction)
def create_promoaction(
    *,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_active_superuser),
    promoaction_in: PromoActionCreate
):
    if current_user.is_superuser:
        promoaction = promoaction_crud.create(db, obj_in=promoaction_in)
        return promoaction


@router.put('/update_promoaction/', response_model=PromoAction)
def update_promoaction(
    *,
    db: Session = Depends(get_db),
    id: int,
    promoaction_in: PromoActionUpdate,
    current_user: UserModel = Depends(get_current_active_superuser)
):
    promoaction = promoaction_crud.get_by_id(db, id=id)
    if not promoaction:
        raise HTTPException(
            status_code=404,
            detail='Промоакции с таким id не найдено',
        )

    if current_user.is_superuser:
        promoaction = promoaction_crud.update(
            db, db_obj=promoaction, obj_in=promoaction_in
            )
        return promoaction


@router.delete('/delete_promoaction/', response_model=PromoAction)
def delete_promoaction(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: UserModel = Depends(get_current_active_superuser)
):
    promoaction = promoaction_crud.get_by_id(db, id=id)
    if not promoaction:
        raise HTTPException(
            status_code=404,
            detail='Промоакции с таким id не найдено',
        )
    if current_user.is_superuser:
        promoaction = promoaction_crud.delete(db, id=id)
        return promoaction
