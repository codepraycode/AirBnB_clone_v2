#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import models

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""


        if len(kwargs) == 0:
            # If no object template is given
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            # Assign template data to instance
            
            # preserve existing created_at
            if kwargs.get("created_at"):
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.created_at = datetime.now()

            # preserve existing updated_at
            if kwargs.get("updated_at"):
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.updated_at = datetime.now()

            if not kwargs.get("id"):
                self.id = str(uuid.uuid4())

            for obj, obj_val in kwargs.items():
                if "__class__" not in obj:
                    setattr(self, obj, val)

    def __str__(self):
        """Returns a string representation of the instance"""
        # cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        # return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)
        return ("[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id, self.__dict__))
    
    def __repr__(self):
        """Returns a string representation of the instance"""
        return ("[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """Updates updated_at with current time when instance is changed"""

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = dict(self.__dict__)
        dictionary['__class__'] = self.__class__.__name__

        dictionary['created_at'] = self.created_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")

        dictionary['updated_at'] = self.updated_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")

        if "_sa_instance_state" in dictionary.keys():
            del dictionary["_sa_instance_state"]

        return dictionary
    
    def delete(self):
        """Delete the current instance from storage"""
        models.storage.delete(self)
