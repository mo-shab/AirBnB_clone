#!/usr/bin/python3
"""Unittest module for Place class"""

from models.base_model import BaseModel
from models.place import Place
import unittest
import pep8
import os


class TestPlace(unittest.TestCase):
    """Class to test Place"""

    @classmethod
    def setUpClass(cls_instance):
        """Function that defines instructions within unittests"""

        cls_instance.place = Place()
        cls_instance.place.city_id = "MA"
        cls_instance.place.user_id = "13"
        cls_instance.place.name = "Maamoura Coast"
        cls_instance.place.description = "Beach House"
        cls_instance.place.number_rooms = 6
        cls_instance.place.number_bathrooms = 6
        cls_instance.place.max_guest = 6
        cls_instance.place.price_by_night = 50
        cls_instance.place.latitude = 1.3
        cls_instance.place.longitude = 3.1
        cls_instance.place.amenity_ids = []

    @classmethod
    def tearDownClass(cls_instance):
        """Function that removes setup class"""

        del cls_instance.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style(self):
        """Function that checks if file is pep8"""

        f_style = pep8.StyleGuide(quiet=True)
        style = f_style.check_files(['models/place.py'])
        self.assertEqual(style.total_errors, 0, "fix pep8")

    def test_subclass(self):
        """Function that checks if class is a subclass of basemodel"""

        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_doc_string(self):
        """Function that checks for functions"""

        self.assertIsNotNone(Place.__doc__)

    def test_attributes(self):
        """Function that tests attributes"""

        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def test_string_attributes(self):
        """Function that tests string attributes"""

        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_save(self):
        """Function that tests saving to json file"""

        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict(self):
        """Fuction that tests dictionary objects of instances in basemodel"""

        self.assertEqual('to_dict' in dir(self.place), True)


if __name__ == "__main__":
    unittest.main()
