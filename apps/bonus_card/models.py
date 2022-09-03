from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from core.db import Base


class BonusCard(Base):
    __tablename__ = 'bonus_card'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='bonus_card')
