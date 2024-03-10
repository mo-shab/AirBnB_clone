#!/usr/bin/python3
"""Unittest modlue for Amenity class"""

from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
import pep8
import os


class TestAmenity(unittest.TestCase):
    """Class to test Amenity."""

    @classmethod
    def setUpClass(cls_instance):
        """Function that defines instructions within unittests"""

        cls_instance.amenity = Amenity()
        cls_instance.amenity.name = "Swimming Pool"

    @classmethod
    def tearDownClass(cls_instance):
        """Function that removes setup class."""

        del cls_instance.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style(self):
        """Function that checks if file is pep8"""

        f_style = pep8.StyleGuide(quiet=True)
        style = f_style.check_files(['models/amenity.py'])
        self.assertEqual(style.total_errors, 0, "fix pep8")

    def test_subclass(self):
        """Function that checks if class is a subclass of basemodel"""

        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_doc_string(self):
        """Function that checks for functions"""

        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes(self):
        """Function that tests attributes"""

        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_string_attributes(self):
        """Function that tests string attributes"""

        self.assertEqual(type(self.amenity.name), str)

    def test_save(self):
        """Function that tests savong of json file"""

        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict(self):
        """Function that tests dictionary objects of instances in basemodel"""

        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
