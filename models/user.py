#!/usr/bin/python3
"""
user module
Contains the User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    The User class inherits from BaseModel

    Attributes:
    """


    def __init__(self, *args, **kwargs):
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        super().__init__(**kwargs)
