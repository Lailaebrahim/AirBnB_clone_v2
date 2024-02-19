#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """DataBase storage object"""
    __engine = None
    __session = None

    def __init__(self):
        """Class Constructor"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all objects depending on the class name (argument cls)
        The is operator checks if cls is a string, and if it is,
         the eval function is used to convert the string to a class object"""
        obj_dict = {}
        if cls:
            cls = globals().get(cls)
            query = self.__session.query(cls)
            for instance in query:
                key = "{}.{}".format(type(instance).__name__, instance.id)
                obj_dict[key] = instance
        else:
            tables = [State, City, User, Place, Review, Amenity]
            for obj_class in tables:
                query = self.__session.query(obj_class)
                for instance in query:
                    key = "{}.{}".format(type(instance).__name__, instance.id)
                    obj_dict[key] = instance
        return obj_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
