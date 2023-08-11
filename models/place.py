#!/usr/bin/python3
"""
place module
Contains the Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    a place
    Inherits from BaseModel class
    """

    def __init__(self, *args, **kwargs):
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        amenity_ids = [""]
