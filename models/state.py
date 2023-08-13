#!/usr/bin/python3
"""
state module
Contains the State class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    A state/region
    Inherits from BaseModel

    Attributes:
        name (str): The of the state where the place is located
    """
    name = ""
