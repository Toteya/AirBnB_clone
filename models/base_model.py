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
        updated_at (datetime): The date and time when the object was
    """

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

        Args:
            *args: list of arguments
            **kwargs: dict of key-values arguments
        """
            Time_form = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, Time_form)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            self.save()

    def __str__(self):
        """
        Returns official string representation of the BaseModel instance
        """
        Class_Name = self.__class__.__name__
        return "[{}] ({}) {}".format(Class_Name, self.id, self.__dict__)

    def save(self):
        """
        Updates the date and time that the instance was modified
        """
        self.updated_at = str(datetime.isoformat(datetime.today()))

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the
        BaseModel instance, including the class.
        """
        bm_dict = self.__dict__
        bm_dict['__class__'] = self.__class__
        return bm_dict
