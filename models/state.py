#!/usr/bin/python3
"""
state module
Contains the State class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    A state/region
    Inherits from BaseModel
    """

    def __init__(self, **kwargs):
        self.name = ""
        super().__init__(**kwargs)
