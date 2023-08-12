#!/usr/bin/python3
"""
The review module contains the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    defines a user review
    Inherits from BaseModel
    """

    def __init__(self, *args, **kwargs):
        self.place_id = ""
        self.user_id = ""
        super().__init__(**kwargs)
