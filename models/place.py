#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        amenity_ids = []

        @property
        def reviews(self):
            """the FileStorage relationship between Place and Review."""
            from models.__init__ import storage
            list_obj = []
            objs = storage.all('Review')
            for key, val in objs.items():
                if val.place_id == self.id:
                    list_obj.append(val)
            return list_obj

        @property
        def amenities(self):
            """Returns the list of Amenity instances based on
            the attribute amenity_ids
            that contains all Amenity.id linked to the Place"""
            from models.__init__ import storage
            list_obj = []
            objs = storage.all('Amenity')
            list_obj = [objs[obj_id] for obj_id in self.amenity_ids
                        if obj_id in objs]
            return list_obj

        @amenities.setter
        def amenities(self, obj):
            """handle appending an amenity_id to the amenities_ids list"""
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
            else:
                pass
