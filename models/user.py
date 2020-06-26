#!/usr/bin/env python3
""" User Class """
from models.base_model import BaseModel
from models import storage

class User(BaseModel):
    """ User class inherits from BaseModel class """

    def __init__(self, **kwargs):
#        super.__init__(kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
