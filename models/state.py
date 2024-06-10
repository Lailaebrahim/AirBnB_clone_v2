#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade='all, delete, delete-orphan',
                              backref="state")
    else:

        @property
        def cities(self):
            from models import storage
            list_obj = []
            objs = storage.all('City')
            for key, val in objs.items():
                if val.state_id == self.id:
                    list_obj.append(val)
            return list_obj
