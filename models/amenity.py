#!/usr/bin/python3
"""
amenity module
Contains the Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    An amenity offered at a place
    Inherits from BaseModel class

    Attributes:
        name (str): The name of the amenity
    """
    name = ""
