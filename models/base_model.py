#!/usr/bin/python3

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

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

        Args:
            *args: list of arguments
            **kwargs: dict of key-values arguments
        """
            self.id = str(uuid.uuid4())

    def __str__(self):
        """
        Returns official string representation of the BaseModel instance
        """
        Class_Name = self.__class__.__name__
        return "[{}] ({}) {}".format(Class_Name, self.id, self.__dict__)
