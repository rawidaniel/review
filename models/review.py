#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Float
class Review(BaseModel, Base):
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=True)
    rate = Column(Float, nullable=False)
    food_id = Column(String(60), ForeignKey('foods.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'),nullable = False)

    def __init__(self, *args, **kwargs):
        """initializes review"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.text)