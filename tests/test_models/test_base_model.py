#!/usr/bin/python3
""" Unit test BaseModel
"""
import unittest
import models
from models.base_model import BaseModel



class TestBaseModel(unittest.TestCase):
    """
    Test Cases for Class BaseModel
    """

    def test_init_BaseModel(self):
        """
        test if an object is BaseModel
        """
        objt = BaseModel()
        self.assertIsInstance(objt, BaseModel)

    def test_str(self):
        """
        test if output is in the specified format
        """
        my_obj = BaseModel()
        _dict = my_obj.__dict__
        str1 = "[BaseModel] ({}) {}".format(my_obj.id, _dict)
        str2 = str(my_obj)
        self.assertEqual(str1, str2)

    def test_save(self):
        """ check if date update when save """
        my_objectupd = BaseModel()
        first_updated = my_objectupd.updated_at
        my_objectupd.save()
        second_updated = my_objectupd.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        """check if to_dict returns a dictionary, if add a class
        key with class name of the object and if updated_at and
        created_at are converted to string object in ISO format."""
        my_model3 = BaseModel()
        my_dict_model3 = my_model3.to_dict()
        self.assertIsInstance(my_dict_model3, dict)
        for key, value in my_dict_model3.items():
            flag = 0
            if my_dict_model3['__class__'] == 'BaseModel':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model3.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
