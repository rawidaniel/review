#!/usr/bin/python3
'''
    Package initializer
'''
from models.base_model import BaseModel
from models.food import Food
from models.restaurant import Restaurant
from models.review import Review
from models.user import User
from models.database import db_storage

storage = db_storage.DBStorage()

classes = {"BaseModel": BaseModel, "User": User,
           "Food": Food, "Restaurant": Restaurant,
           "Review": Review}

storage.create()
