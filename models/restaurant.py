#!/usr/bin/python3
""" holds class Restaurant"""
from models.base_model import BaseModel,Base
from sqlalchemy import Column, String, Table, ForeignKey, BLOB, Unicode
from sqlalchemy.orm import relationship

# restaurant_food = Table("restaurant_food",Base.metadata,
#                         Column("restaurant_id", String(60), ForeignKey('restaurants.id'),
#                                 primary_key=True, nullable=False),
#                         Column("food_id", String(60), ForeignKey('foods.id'),
#                                 primary_key=True, nullable=False))
class Restaurant(BaseModel, Base):
    __tablename__ = 'restaurants'
    name = Column(String(75), nullable=False)
    address = Column(String(100), nullable=False)
    description = Column(String(1024),nullable=False )
    image = Column(String(100), nullable=False)
    contact = Column(String(100), nullable=False)
    foods = relationship('Food', backref='restaurant',
                        cascade='all, delete, delete-orphan')
#   foods = relationship('Food', secondary=restaurant_food,
#                           viewonly=False, back_populates='restaurants')

    def __init__(self, *args, **kwargs):
        """initializes restaurant"""
        super().__init__(*args, **kwargs)
    
    def __str__(self):
        return "{}".format(self.name)