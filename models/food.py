#!/usr/bin/python3
""" holds class Food"""
from models.base_model import BaseModel, Base
# from models.restaurant import restaurant_food
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Food(BaseModel, Base):
    __tablename__ = 'foods'
    name = Column(String(60), nullable=False)
    price = Column(Float, nullable=False)
    recipe = Column(String(120), nullable=False)
    description = Column(String(500), nullable=False)
    image = Column(String(100), nullable=False)
    restaurant_id = Column(String(60), ForeignKey('restaurants.id'),nullable = False)
    reviews = relationship('Review', backref='food',
                          cascade='all, delete, delete-orphan')
    # restaurants = relationship('Restaurant', secondary=restaurant_food,
    #                       viewonly=False, back_populates='foods')

    def __init__(self, *args, **kwargs):
        """initializes food"""
        super().__init__(*args, **kwargs)
    def __str__(self):
        return "{}".format(self.name)