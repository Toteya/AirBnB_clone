"""
base_model module
Contains the BaseModel class
"""
import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class
    Defines all common attributes/methods for other classes

    Attributes:
        id (str): The unique identifier of the BaseModel instance
            generated with uuid4
        created_at (datetime): The date and time when the object was created
        updated_at (datetime): The date and time when the object was modified
    """

    def __init__(self):
        pass

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance
        """
        pass

    def __save_(self):
        """
        Updates the instance attribute `updated_at` with the current
        datetime
        """
        pass

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the
        BaseModel instance, including the class.
        """
        pass
