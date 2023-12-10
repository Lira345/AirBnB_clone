#!/usr/bin/python3
""" Review module for the HolbertonBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Reviews class to store review info """
    place_id = ""
    user_id = ""
    text = ""
