#!/usr/bin/python3
"""Module of Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class that defines Review instance attribute."""

    place_id = ""
    user_id = ""
    text = ""
