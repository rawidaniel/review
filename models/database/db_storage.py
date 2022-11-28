#!/usr/bin/python3
"""
    Define class DatabaseStorage
"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.base_model import Base
from models.food import Food
from models.restaurant import Restaurant
from models.review import Review
from models.user import User


class DBStorage:
    """
        Create SQLalchemy database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
            Create engine and link to MySQL databse (hbnb_dev, hbnb_dev_db)
        """
        user = getenv("HBNB_MYSQL_USER", "hbnb_addis_review")
        pwd = getenv("HBNB_MYSQL_PWD", "addisreview")
        host = getenv("HBNB_MYSQL_HOST", "localhost")
        db = getenv("HBNB_MYSQL_DB", "hbnb_addis_review_db")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)

    def all(self, cls=None):
        """
            Query current database session
        """
        db_dict = {}

        if cls != "":
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                db_dict[key] = obj
            return db_dict
        else:
            for k, v in models.classes.items():
                if k != "BaseModel":
                    objs = self.__session.query(v).all()
                    if len(objs) > 0:
                        for obj in objs:
                            key = "{}.{}".format(obj.__class__.__name__,
                                                 obj.id)
                            db_dict[key] = obj
            return db_dict

    def new(self, obj):
        """
            Add object to current database session
        """
        self.__session.add(obj)

    def save(self):
        """
            Commit all changes of current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
            Delete from current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def create(self):
        """
            Commit all changes of current database session
        """
        self.__session = Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def get_user_by_email(self, email):
        """
            Reterive object based on user email
        """
        user = self.__session.query(User).filter_by(email=email).first()
        return user

    def get_user_by_id(self, id):
        """
            Reterive user object based on provided user id
        """
        user = self.__session.query(User).get(id)
        return user

    def session(self):
        """
            Reterive the session
        """
        return self.__session

    def close(self):
        """
            Remove private session attribute
        """
        self.__session.close()

    def get(self, cls, id):
        """
            Reterive object based on the class and its ID
        """
        result = None
        try:
            for clss in models.classes:
                if cls is clss or cls is models.classes[clss]:
                    objs = self.__session.query(models.classes[clss]).all()
                    for obj in objs:
                        if id == obj.id:
                            result = obj
        except BaseException:
            pass
        return result

    def count(self, cls=None):
        """
            Reterive the number of objects in storage
        """
        count = 0
        for clss in models.classes:
            if clss != "BaseModel":
                if cls is None or cls is clss or cls is models.classes[clss]:
                    objs = self.__session.query(models.classes[clss]).all()
                    for obj in objs:
                        count += 1
        return count
