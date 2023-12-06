#!/usr/bin/python3
"""Define the Review class"""
from models.base_model import BaseModel

class Review(BaseModel):
    """This is a description of review

    Attributes:
         place_id (str): The pointer to Place id.
         user_id (str): The pointer to User id.
         text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
