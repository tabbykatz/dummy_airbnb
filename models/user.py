#!/usr/bin/env python3
""" User Class """
from models.base_model import BaseModel
from models import storage

class User(BaseModel):
    """ User class extends BaseModel """
        email = ""
        password = ""
        first_name = ""
        last_name = ""
