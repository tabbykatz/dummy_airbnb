#!/usr/bin/env python3
""" File Storage module """
from datetime import datetime
<<<<<<< HEAD
<<<<<<< HEAD
import json
=======
>>>>>>> cynthia_working
=======
>>>>>>> 8fc030dbbf10fd4555599549edb02fe0546a1348
import os
import json

class FileStorage:
    """ File Storage Class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
<<<<<<< HEAD
<<<<<<< HEAD
        """ Returns the dictionary __objects"""
=======
        """ Returns the dictionary __objects """
>>>>>>> cynthia_working
=======
        """ Returns the dictionary __objects """
>>>>>>> 8fc030dbbf10fd4555599549edb02fe0546a1348
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with the key <obj class name>.id """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def classes(self):
        """ Returns a dict of all valid classes """
        from models.base_model import BaseModel
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        from models.user import User

        classes = {"BaseModel": BaseModel,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review,
                   "User": User}
        return classes

    def save(self):
        """ serializes __objects to the JSON file (path __file_path) """
        with open(FileStorage.__file_path, "w") as f:
            my_dict = {key: val.to_dict() for key, val in
                 FileStorage.__objects.items()}
            json.dump(my_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists) """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as f:
            try:
                obj_dict = json.load(f)
            except:
                return
            obj_dict = {k: self.classes()[v["__class__"]](**v) for k, v in
                        obj_dict.items()}
            FileStorage.__objects = obj_dict
