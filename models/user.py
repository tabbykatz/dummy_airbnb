#!/usr/bin/env python3
""" User Class """
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
<<<<<<< HEAD
    """ User class inherits from BaseModel class """

    def __init__(self, **kwargs):
#        super.__init__(kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
=======
    """ User class extends BaseModel """
        email = ""
        password = ""
        first_name = ""
        last_name = ""
>>>>>>> e3b4cd2ce3b4c28ad27cc7d4d7ae8db4a9a1e0d6
=======
    """ User class inherits from BaseModel class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
>>>>>>> 8fc030dbbf10fd4555599549edb02fe0546a1348
