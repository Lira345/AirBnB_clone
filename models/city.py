#!/usr/bin/python3
"""Define the city class"""
from models.base_model import BaseModel

class City(BaseModel):
    """This represents the city class

    Attributes:
         state_id (str): Pointer to state id.
         name (str): Pointer to the name of the city.
    """

    state_id = ""
    name = ""
