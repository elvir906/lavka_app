from sqlalchemy import Boolean, Column, Integer, String
from core.db import Base


class PromoAction(Base):
    __tablename__ = "promoaction"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    type = Column(String, nullable=False)
    iconpath = Column(String, nullable=False)
    imagepath = Column(String, nullable=False)
    subtitle = Column(String, nullable=False)
    attention_text = Column(String, nullable=False)
    description = Column(String, nullable=False)
    sort = Column(Integer, index=True)
    is_active = Column(Boolean, default=False)
