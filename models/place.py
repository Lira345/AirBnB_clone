#!/usr/bin/python3
"""Define the Place class"""
from models.base_model import BaseModel

class Place(BaseModel):
    """This represents a place class

    Attributes:
         city_id (str): The pointer to City id.
         user_id (str): The pointer to User id.
         name (str): The pointer to name of the place.
         description (str): The represantion of the place.
         number_rooms (int): The number of rooms in the place.
         number_bathrooms (int): The number of bathrooms in the place.
         max_guest (int): The maximum number of guests supposed to be in place.
         price_by_night (int): The price by night of the place.
         latitude (float): The latitude in the place.
         longitude (float): The longitude in the place.
         amenity_ids (list): A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
