#!/usr/bin/python3
""" holds class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


class User(BaseModel, Base, UserMixin):
    """The User class"""
    __tablename__ = 'users'
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False)
    password = Column(String(120), nullable=False)
    is_admin = Column(Boolean, default=False)
    reviews = relationship('Review', backref='user',
                           cascade='all, delete, delete-orphan')

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with sha256 enryption"""
        if name == "password":
            value = generate_password_hash(value, method='sha256')
        super().__setattr__(name, value)

    def __str__(self):
        """String representation of the User class"""
        return "{} {}".format(self.first_name, self.last_name)
