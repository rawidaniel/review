#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
class Review(BaseModel, Base):
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    food_id = Column(String(60), ForeignKey('foods.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'),nullable = False)