#!/usr/bin/python3
"""Define the User class"""
from models.base_model import BaseModel

class User(BaseModel):
    """This is a description of a User.

    Attributes:
        email (str): The pointer to the email of the user.
        password (str): The pointer to the password of the user.
        first_name (str): The pointer to first name of the user.
        last_name (str): The pointer to last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
