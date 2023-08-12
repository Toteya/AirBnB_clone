#!/usr/bin/python3
"""Module for review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """represent about the reviews     

    Attributes:
        place_id (str): id of the place
        user_id (str): User id.        
        text (str): review text        
    """

    place_id = ""
    user_id = ""
    text = ""
