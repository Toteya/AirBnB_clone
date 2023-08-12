#!/usr/bin/python3
"""module for amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenity representation.

    Attributes:
        name (str): amenit's name      
    """

    name = ""
