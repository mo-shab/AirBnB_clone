#!/usr/bin/python3
"""
Module : File Storage
"""


class FileStorage:
    """
    Class FileStorage define all storage related
    functions
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        function all that dict _objects
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        """

