#!/usr/bin/python3
""" holds class Review"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Float


class Review(BaseModel, Base):
    """The Review class"""
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=True)
    rate = Column(Float, nullable=False)
    food_id = Column(String(60), ForeignKey('foods.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes review"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """String representation of the Review class"""
        return "(*{}) {}".format(self.rate, self.text)
