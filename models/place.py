#!/usr/bin/python3
"""
Module - place
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """class Place"""
    city_id = ""
    user_id = ""
    name = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = float(0)
    longitude = float(0)
    amenity_ids = []