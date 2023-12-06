#!/usr/bin/python3
"""Define the State class"""
from models.base_model import BaseModel

class State(BaseModel):
    """The description of the state

    Attributes:
        name (str): The pointer to the name of the state.
    """

    name = ""
