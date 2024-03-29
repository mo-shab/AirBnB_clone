#!/usr/bin/python3
"""Module BaseModel class and instances"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Class that defines Base Model"""

    def __init__(self, *args, **kwargs):
        """Function to initialize instance public attributes"""

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")

                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

                else:
                    self.__dict__[key] = kwargs[key]

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Function that returns official string rep of instances"""

        return ("[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__))

    def save(self):
        """Function to update public instance attributes with updated date"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Function that returns a dict with key/value pairs of instances"""

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return (new_dict)
