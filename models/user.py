#!/usr/bin/env python3
""" User Class """
from models.base_model import BaseModel

class User(BaseModel):
    """ User class inherits from BaseModel class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
