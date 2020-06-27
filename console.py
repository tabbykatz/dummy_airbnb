#!/usr/bin/env python3
""" Console Module """

import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """ Class for the console """

    prompt = "(hbnb) "

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        if line is "" or line is None:
            print("** class name missing **")
        else:
            terms = line.split(' ')
            if terms[0] not in storage.classes():
                print("** cllass doesn't exist **")
            elif len(terms) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(terms[0], terms[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """ Displays all instances, optionally, display all of a class of
        instances."""
        if line is not "":
            terms = line.split(' ')
            if terms[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                obj_list = [str(obj) for key, obj in storage.all().items() if
                            type(obj.__name__ == terms[0])]
                print(obj_list)
        else:
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
