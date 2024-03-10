#!/usr/bin/python3
"""Unittest module for Review class"""

from models.base_model import BaseModel
from models.review import Review
import unittest
import pep8
import os


class TestReview(unittest.TestCase):
    """Class to test Review"""

    @classmethod
    def setUpClass(cls_instance):
        """Function that defines instructions within unittests"""

        cls_instance.review = Review()
        cls_instance.review.place_id = "MA"
        cls_instance.review.user_id = "HAN-13"
        cls_instance.review.text = "5 Star"

    @classmethod
    def tearDownClass(cls_instance):
        """Function that removes setup class"""

        del cls_instance.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style(self):
        """Function to check if file is pep8"""

        f_style = pep8.StyleGuide(quiet=True)
        style = f_style.check_files(['models/review.py'])
        self.assertEqual(style.total_errors, 0, "fix pep8")

    def test_subclass(self):
        """Function that checks if class is a subclass of basemodel"""

        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_doc_string(self):
        """Function that tests functions"""

        self.assertIsNotNone(Review.__doc__)

    def test_attributes(self):
        """Function that tests attributes"""

        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)

    def test_string_attributes(self):
        """Function that tests string attributes"""

        self.assertEqual(type(self.review.text), str)
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)

    def test_save(self):
        """Function that tests saving to json file"""

        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_to_dict(self):
        """Fuction that tests dictionary objects of instances in basemodel"""

        self.assertEqual('to_dict' in dir(self.review), True)


if __name__ == "__main__":
    unittest.main()
