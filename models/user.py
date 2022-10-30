#!/usr/bin/python3
"""
Module - User
"""


from models.base_model import BaseModel


class User(BaseModel):
    """class User"""
    email = ""
    password = ""
    string = ""
    first_name = ""
    last_name = ""
