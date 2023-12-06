#!/usr/bin/python3
"""Define the Amenity class"""+

from models.base_model import BaseModel

class Amenity(BaseModel):
    """This represents the amenity class.

    Attributes:
        name (str): The pointer to the name of the amenity.
    """

    name = ""
