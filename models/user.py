#!/usr/bin/python3
"""Module for the class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """this class should be a user
    of the page
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
