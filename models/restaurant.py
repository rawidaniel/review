#!/usr/bin/python3
""" holds class Restaurant"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey, BLOB, Unicode
from sqlalchemy.orm import relationship


class Restaurant(BaseModel, Base):
    """The Restaurant class"""
    __tablename__ = 'restaurants'
    name = Column(String(75), nullable=False)
    address = Column(String(100), nullable=False)
    description = Column(String(1024), nullable=False)
    image = Column(String(100), nullable=False)
    contact = Column(String(100), nullable=False)
    foods = relationship('Food', backref='restaurant',
                         cascade='all, delete, delete-orphan')

    def __init__(self, *args, **kwargs):
        """initializes restaurant"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """String representation of the Restaurant class"""
        return "{}".format(self.name)
