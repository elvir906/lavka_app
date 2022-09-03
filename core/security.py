from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from . settings import EnvData


ALGORITHM = 'HS256'
access_token_jwt_subject = 'access'


def create_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire, 'sub': access_token_jwt_subject})
    return jwt.encode(to_encode, EnvData.secret, algorithm=ALGORITHM)


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)
