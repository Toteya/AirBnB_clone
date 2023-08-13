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

    Attributes:
        state_id (str): The unique id of the State in which the city is.
        name (str): The name of the city
    """

    id = ""
    name = ""
