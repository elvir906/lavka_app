from fastapi import APIRouter
from apps.base.schemas import Msg


router = APIRouter()


@router.post("/hello", response_model=Msg, status_code=201)
def test_hello():
    return {"msg": "Hello Wordl"}
