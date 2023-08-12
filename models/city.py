#!/usr/bin/python3
"""
city module
Contains the city class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A city
    Inherits from BaseModel class
    """

    def __init__(self, *args, **kwargs):
        self.id = ""
        self.name = ""
        super().__init__(**kwargs)
