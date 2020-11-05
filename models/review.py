"""Module for the class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """this is a class for the review
    of the page
    """
    place_id = ""
    user_id = ""
    text = ""
