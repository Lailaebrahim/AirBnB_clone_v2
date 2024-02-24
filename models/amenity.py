#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place, place_amenity
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Define Amenity Class"""
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity
                                   , back_populates="amenities")
