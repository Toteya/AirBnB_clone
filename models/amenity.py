#!/usr/bin/python3
"""
amenity module
Contains the Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    amenity class
    Inherits from BaseModel class
    """

    def __init__(self, *args, **kwargs):
        self.name = ""
        super().__init__(**kwargs)
