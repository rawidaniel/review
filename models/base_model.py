#!/usr/bin/python3
"""
holds class BaseModel
"""
import uuid
from datetime import datetime as dt
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models
time = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()


def generate_uuid():
    """return UUID value converted to string"""
    return str(uuid.uuid4())


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    id = Column(String(75), nullable=False, primary_key=True,
                default=generate_uuid)
    created_on = Column(DateTime, default=dt.utcnow, nullable=False)
    updated_on = Column(DateTime, default=dt.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = dt.strptime(kwargs["created_at"], time)
            else:
                self.created_at = dt.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = dt.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = dt.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_on = dt.now()
            self.updated_on = dt.now()

    def save(self):
        """save object"""
        self.updated_on = dt.now()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Delete object"""
        models.storage.delete(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                new_dict[key] = val.isoformat()
            else:
                new_dict[key] = val
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if "password" in new_dict:
            del new_dict["password"]
        return new_dict

    def __str__(self):
        """String representation of the BaseModel class"""
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)
