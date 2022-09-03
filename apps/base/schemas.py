from pydantic.main import BaseModel
from typing import Optional


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    user_id: Optional[int] = None
    exp: Optional[int] = None
    sub: Optional[str] = None


class Msg(BaseModel):
    msg: str
