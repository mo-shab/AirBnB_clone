#!/usr/bin/python3
"""Unittest module for FileStorage Class"""

from models.engine.file_storage import FileStorage
from models.user import User
import unittest
import json
import pep8
import os


class TestFileStorage(unittest.TestCase):
    """Class to test FileStorage"""

    @classmethod
    def setUpClass(cls_instance):
        """Function that assigns variables to instances"""

        cls_instance.user = User()
        cls_instance.user.email = "user@test.com"
        cls_instance.user.password = "test"
        cls_instance.user.first_name = "Lionel"
        cls_instance.user.last_name = "Messi"
        cls_instance.storage = FileStorage()

    @classmethod
    def teardown(self):
        """Function that removes setup variables from file"""

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style(self):
        """Function that checks if file is pep8"""

        f_style = pep8.StyleGuide(quiet=True)
        style = f_style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(style.total_errors, 0, "not pep8")

    def test_all(self):
        """Function that tests all instance"""

        storage = FileStorage()
        all_dict = storage.all()
        self.assertIsNotNone(all_dict)
        self.assertEqual(type(all_dict), dict)
        self.assertIs(all_dict, storage._FileStorage__objects)

    def test_new(self):
        """Function that tests new instance"""

        storage = FileStorage()
        all_dict = storage.all()
        user = User()
        user.name = "Messi"
        user.id = 10
        storage.new(user)
        user_key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(all_dict[user_key])

    def test_reload(self):
        """Function that tests reload instance"""

        self.storage.save()
        cpath = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(cpath, "file.json")
        with open(path, "r") as f:
            line1 = f.readlines()

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

        self.storage.save()

        with open(path, "r") as f:
            line2 = f.readlines()

        self.assertEqual(line1, line2)

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

        with open(path, "w") as f:
            f.write("{}")

        with open(path, "r") as f:
            for line in f:
                self.assertEqual(line, "{}")

        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
