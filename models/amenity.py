#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from constants.env import STORAGE_TYPE
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place

class Amenity(BaseModel, Base):

    """Amenities class
    """

    __tablename__ = "amenities"

    if STORAGE_TYPE == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity")
    else:
        name = ""
