#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from constants.env import STORAGE_TYPE
from .review import Review
# from models.amenity import Amenity


association_table = Table("place_amenity", Base.metadata,
                        Column("place_id", String(60),
                                ForeignKey("places.id"),
                                primary_key=True, nullable=False),
                        Column("amenity_id", String(60),
                            ForeignKey("amenities.id"),
                            primary_key=True, nullable=False))



class Place(BaseModel, Base):
    """ A place to stay """
    
    __tablename__ = "places"

    if STORAGE_TYPE == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer(), default=0, nullable=False)
        number_bathrooms = Column(Integer(), default=0, nullable=False)
        max_guest = Column(Integer(), default=0, nullable=False)
        price_by_night = Column(Integer(), default=0, nullable=False)
        latitude = Column(Float())
        longitude = Column(Float())

        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity", secondary="place_amenity",
                                   viewonly=False)
        amenity_ids = []
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
    
    if STORAGE_TYPE != 'db':
        @property
        def reviews(self):
            """Returns a list of Reviews instances related to Place instance
            """
            _reviews = []
            all_reviews = storage.all(Review)
            for each_review in all_reviews.values():
                if each_review.place_id == self.id:
                    _reviews.append(each_review)
            return _reviews
        
        @property
        def amenities(self):
            """Get/set linked Amenities."""
            amenity_list = []
            for amenity in list(models.storage.all(models.Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
