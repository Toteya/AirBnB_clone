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

    Attributes:
        city_id (str): The unqique id of the city where the place is located
        user_id (str): The unique id of the user
        name (str): The name of the place
        description (str): A description of the place
        number_rooms (int): The total number of rooms at place
        number_bathrooms (int): Number of bathrooms
        max_guest (int): Maximum number of guests the place can accomodate
        price_by_night (float): Price per night
        latitude (float): Coordinates - latitude
        longitude (float): Coordinates - longitude
        amenity_ids (list: str): List of amenities offered at the place
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
