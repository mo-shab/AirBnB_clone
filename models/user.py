#!/usr/bin/python3
"""Module of the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class that defines User instance attributes"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
