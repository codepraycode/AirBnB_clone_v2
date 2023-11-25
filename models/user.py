#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from constants.env import STORAGE_TYPE
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = "users"

    if STORAGE_TYPE == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
