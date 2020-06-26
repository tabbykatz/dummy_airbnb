#!/usr/bin/env python3
""" Console Module """

import cmd
from models.base_model import BaseModel
from models import storage
import json

class HBNBCommand(cmd.Cmd):
    """ Class for the console """

    prompt = "(hbnb) "

    def do_all(self, line):
        """ Displays all instances, optionally, display all of a class of
        instances."""
        obj_list = [str(obj) for key, obj in storage.all().items()]
        print(obj_list)

    def do_create(self, line):
        """Creates a new instance. """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            inst = BaseModel()
            inst.save()
            print(inst.id)

    def do_EOF(self, line):
        """End-of-file input exits console. """
        print()
        return True

    def do_quit(self, line):
        """Use quit to exit console. """
        return True

    def emptyline(self):
        """Prints an empty line. """
        print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
