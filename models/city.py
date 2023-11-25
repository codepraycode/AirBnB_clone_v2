#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


STORAGE_TYPE = getenv("HBNB_TYPE_STORAGE")

class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"

    if STORAGE_TYPE == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete, delete-orphan")

    else:
        state_id = ""
        name = ""
