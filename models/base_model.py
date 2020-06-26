#!/usr/bin/env python3
""" Base Class """
from json import dumps, loads
import uuid
from datetime import datetime
from models import storage

tf = "%Y-%m-%dT%H:%M:%S.%f" #time format

class BaseModel:
    """ Base Class """

    def __init__(self, **kwargs):
        """ init a Base Instance """

        if kwargs:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], tf)
                if key == 'updated_at':
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], tf)
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = uuid.uuid4()
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Print a Base Model"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute 'updated_at' with the
        current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__
        of the instance """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
