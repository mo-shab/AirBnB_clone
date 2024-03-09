#!/usr/bin/python3
"""
Module : File Storage
"""
import json
import os
from models.base_model import BaseModel


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
        all_objs = FileStorage.__objects
        obj_dict = {}
        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)


    def reload(self):
        """
        deserializes the JSON file to _objects
        Only if JSON file exists, otherwise, do nothing.
        if the file doesn't exist, no exception
        should be raised
        """
        definedClasses = {'BaseModle': BaseModel}
        
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                deserialized = json.load(file)
                for obj_values in deserialized.values():
                    clsName = obj_values["__class__"]
                    cls_obj = definedClasses[clsName]
                    self.new(cls_obj(**obj_values))
        
        except FileNotFoundError:
            pass
