from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.utils import (
    get_current_active_user,
    get_db,
    get_current_active_superuser,
    create_unique_card_code,
)
from apps.user.models import User as ModelUser
from apps.bonus_card.schemas import BonusCard, BonusCardCreate, BonusCardUpdate
from apps.bonus_card.crud import crud_bonus_card


router = APIRouter()


@router.get('/get_card/', response_model=BonusCard)
def read_cards_page_pagesize(
    db: Session = Depends(get_db),
    card_id: int = None,
    current_user: ModelUser = Depends(get_current_active_user)
):
    if current_user.is_superuser:
        card = crud_bonus_card.get_by_id(db, id=card_id)
    return card


@router.get('/get_cards/', response_model=List[BonusCard])
def read_cards(
    db: Session = Depends(get_db),
    page: int = 0,
    page_size: int = 10,
    current_user: ModelUser = Depends(get_current_active_superuser)
):
    if current_user.is_superuser:
        cards = crud_bonus_card.get_all(db, page=page, page_size=page_size)
    return cards


@router.post('/create_card/', response_model=BonusCard)
def create_card(
    *,
    db: Session = Depends(get_db),
    user_id: int,
    current_user: ModelUser = Depends(get_current_active_superuser),
):
    card = crud_bonus_card.get_by_user_id(db, user_id=user_id)
    if card:
        raise HTTPException(
            status_code=400,
            detail='У пользователя уже есть карта',
        )
    if current_user.is_superuser:
        card = BonusCardCreate(
            code=create_unique_card_code(code_lenght=10),
            user_id=user_id
        )
    card = crud_bonus_card.create(db, obj_in=card)
    return card


@router.put('/update_card/', response_model=BonusCard)
def update_card(
    *,
    db: Session = Depends(get_db),
    user_id: int,
    card_in: BonusCardUpdate,
    current_user: ModelUser = Depends(get_current_active_superuser),
):
    card = crud_bonus_card.get_by_user_id(db, user_id=user_id)
    if not card:
        raise HTTPException(
            status_code=404,
            detail='Карты с таким пользователем не существует',
        )
    if current_user.is_superuser:
        card = crud_bonus_card.update(db, db_obj=card, obj_in=card_in)
    return card


@router.delete('/delete_card/', response_model=BonusCard)
def delete_card(
    *,
    db: Session = Depends(get_db),
    user_id: int,
    current_user: ModelUser = Depends(get_current_active_superuser),
):
    if current_user.is_superuser:
        card = crud_bonus_card.get_by_user_id(db, user_id=user_id)
        if not card:
            raise HTTPException(
                status_code=404,
                detail='Карты с таким пользователем не существует',
            )
        card = crud_bonus_card.delete(db, id=card.id)
    return card


@router.get('/get_my/', response_model=BonusCard)
def read_user_me(
    db: Session = Depends(get_db),
    current_user: ModelUser = Depends(get_current_active_user),
):
    card = crud_bonus_card.get_by_user_id(db, user_id=current_user.id)
    return card


@router.post('/create_to_me/', response_model=BonusCard)
def create_card_me(
    *,
    db: Session = Depends(get_db),
    current_user: ModelUser = Depends(get_current_active_user),
):
    card = crud_bonus_card.get_by_user_id(db, user_id=current_user.id)
    if card:
        raise HTTPException(
            status_code=404,
            detail='Карта с таким пользователем уже существует',
        )

    card = BonusCardCreate(
        code=create_unique_card_code(code_lenght=10),
        user_id=current_user.id
    )

    card = crud_bonus_card.create(db, obj_in=card)
    return card
