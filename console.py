#!/usr/bin/env python3
""" Console Module """

import cmd
from models.base_model import BaseModel
from models import storage
import json
import shlex
import re

class HBNBCommand(cmd.Cmd):
    """ Class for the console """

    prompt = "(hbnb) "

    def default(self, line):
        """Handle class.cmd(args) commands """
        if not re.search("\.(\w+)\(", line):
            return
        cl_name = line.split(".")[0]
        cmd = line.split(".")[1].split("(")[0]
        term = line.split("(")[1][:-1]

        if cl_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if cmd == "all":
            self.do_all(cl_name)

        elif cmd == "count":
            count = sum(1 for k, v in storage.all().items() if
                        v.to_dict()["__class__"] == cl_name)
            print(count)

        elif cmd == "show":
            self.do_show(cl_name + " " + term.strip("\""))

        elif cmd == "destroy":
            self.do_destroy(cl_name + " " + term.strip("\""))

        elif cmd == "update":
            # if starts with 'id, {}', then split into id and dict
            if re.match('"[^"]+", {.+}', term):
                term = term.replace("\'", "\"")
                term_dict = json.loads(term.split(", ", 1)[1])
                term_id = cl_name + "." + term.split(", ")[0].strip("\"")
                if term_id not in storage.all().keys():
                    print("** no instance found **")
                    return
                for k, v in term_dict.items():
                    setattr(storage.all()[term_id], k, v)
            # else update at id the attribute with new_value
            else:
                terms = term.split(", ")
                self.do_update(cl_name + " " + terms[0].strip("\"") + " " +
                               terms[1].strip("\"") + " " + terms[2])
        else:
            super().default(line)

    def do_update(self, line):
        """Update an instance based on class name and id.\n"""
        if line == "" or line is None:
            print("** class name missing **")
            return
        terms = shlex.split(line, posix=False)
        if terms[0] not in storage.classes():
            print("** class doesn't exit **")
            return
        elif len(terms) < 2:
            print("** instance id missing **")
            return
        #ok so we have a class and an instance id
        # does key exist
        key = "{}.{}".format(terms[0], terms[1])
        if key not in storage.all():#all().keys()?
            print("** no instance found **")
            return

        if len(terms) < 3:
            print("** attribute missing **")
            return
        elif len(terms) < 4:
            print("** value missing **")
            return
        terms[3] = terms[3].strip("\"")
        storage.all()[key].__dict__[terms[2]] = terms[3]
        storage.save()


    def do_show(self, line):
        """Prints an instance by id.\n"""
        if line is "" or line is None:
            print("** class name missing **")
        else:
            terms = line.split(' ')
            if terms[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(terms) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(terms[0], terms[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.\n"""
        if line is "" or line is None:
            print("** class name missing **")
        else:
            terms = line.split(' ')
            if terms[0] not in storage.classes():
                print("** class doesn't exist **")
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
        """Displays all instances, display all of a class of instances.\n"""
        if line is not "":
            terms = line.split(' ')
            if terms[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                obj_list = [str(obj) for key, obj in storage.all().items() if
                            type(obj).__name__ == terms[0]]
                print(obj_list)
        else:
            obj_list = [str(obj) for key, obj in storage.all().items()]
            print(obj_list)

    def do_create(self, line):
        """Creates a new instance.\n"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            inst = storage.classes()[line]()
            inst.save()
            print(inst.id)

    def do_EOF(self, line):
        """End-of-file input exits console.\n"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Prints an empty line.\n"""
        print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
