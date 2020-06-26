#!/usr/bin/env python3
""" File Storage module """
from datetime import datetime
import os
import json

class FileStorage:
    """ File Storage Class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with the key <obj class name>.id """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path __file_path) """
        with open(FileStorage.__file_path, "w") as f:
            my_dict = {key: val.to_dict() for key, val in
                 FileStorage.__objects.items()}
            json.dumps(my_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists) """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as f:
            obj_dict = json.loads(f)
            from models.base_model import BaseModel
            obj_dict = {k: BaseModel(**v) for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict
