from fastapi import APIRouter

from core.endpoints import (
    hello_msg,
    bonus_card,
    user,
    promo_action,
    login
)


api_router = APIRouter()

api_router.include_router(
    user.router,
    prefix='/user',
    tags=['users']
)
api_router.include_router(
    bonus_card.router,
    prefix='/bonus_card',
    tags=['bonus_cards']
)
api_router.include_router(
    promo_action.router,
    prefix='/promo_action',
    tags=['promo_actions']
)
api_router.include_router(
    hello_msg.router,
    prefix='/test',
    tags=['hello']
)
api_router.include_router(
    login.router,
    prefix='/auth',
    tags=['auth']
)
