from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from core.db import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    family = Column(String)
    patronymic = Column(String)
    phone = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String)
    is_superuser = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    bonus_card = relationship('BonusCard', back_populates='user')
