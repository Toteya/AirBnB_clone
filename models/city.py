#!/usr/bin/python3
"""Module for city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class.

    Attributes:
        state_id (str): state id.
        name (str): city's name.
    """

    state_id = ""
    name = ""
