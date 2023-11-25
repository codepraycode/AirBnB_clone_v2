#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship
# from models import storage


STORAGE_TYPE = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    if STORAGE_TYPE == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                                cascade="all, delete, delete-orphan")
    else:
        name = ""


    if STORAGE_TYPE != 'db':
        @property
        def cities(self):
            """Returns a list of City instances related to state
            """
            _cities = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    _cities.append(city)
            return _cities
