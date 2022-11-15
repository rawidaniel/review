#!/usr/bin/python

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from flask_login import UserMixin

class User(BaseModel, Base, UserMixin):
    __tablename__ = 'users'
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False)
    password = Column(String(120), nullable=False)
    reviews = relationship('Review', backref='user',
                          cascade='all, delete, delete-orphan')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)