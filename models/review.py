#!/usr/bin/python3
"""
The review module contains the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A user/guest review
    Inherits from BaseModel

    Attributes:
        place_id (str): The unique id of the place being reviewd
        user_id (str): The unique id of the user doing the review
        text (str): The contents/body of the review
    """

    place_id = ""
    user_id = ""
    text = ""
