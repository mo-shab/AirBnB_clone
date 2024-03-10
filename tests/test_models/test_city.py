#!/usr/bin/python3
"""Unittest module for City class"""

from models.base_model import BaseModel
from models.city import City
import unittest
import pep8
import os


class TestCity(unittest.TestCase):
    """Class to test City"""

    @classmethod
    def setUpClass(cls_instance):
        """Function that defines instructions within unittests"""

        cls_instance.city = City()
        cls_instance.city.name = "Maamoura"
        cls_instance.city.state_id = "MA"

    @classmethod
    def tearDownClass(cls_instance):
        """Function that removes setup class"""

        del cls_instance.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style(self):
        """Function that checks if file is pep8"""

        f_style = pep8.StyleGuide(quiet=True)
        style = f_style.check_files(['models/city.py'])
        self.assertEqual(style.total_errors, 0, "fix pep8")

    def test_subclass(self):
        """Function that checks if class is subclass of basemodel"""

        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_doc_string(self):
        """Function that checks functions"""

        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        """Function that tests attributes"""

        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_string_attributes(self):
        """Function that tests string attributes"""

        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_save(self):
        """Function that tests saving of json file"""

        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """Function that tests dictionary objects of instances in basemodel"""

        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
