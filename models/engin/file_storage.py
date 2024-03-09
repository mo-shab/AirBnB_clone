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
        set _objects the obj with key
        <obj class name>.id
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        serializes _objects to the JSON file
        """
        

    def reload(self):
        """
        deserializes the JSON file to _objects
        Only if JSON file exists, otherwise, do nothing.
        if the file doesn't exist, no exception should be raised"""
        pass
