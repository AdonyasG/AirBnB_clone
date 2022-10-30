#!/usr/bin/python3
"""
Module - Console
"""

import cmd
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """simple command processor"""
    prompt = '(hbnb) '
    Class = {"BaseModel", "User", "Place", "State", "City",
             "Amenity", "Review"}

    def do_EOF(self, line):
        """Shortcut to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        quit()
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.Class:
            print("** class doesn't exist **")
        else:
            base = eval(line)()
            base.save()
            print(base.id)

    def do_show(self, line):
        """
        Prints the string representation
        of an instance based on the class name and id
        """
        arg = parse(line)
        if len(line) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.Class:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg[0]+"."+arg[1] not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[arg[0]+"."+arg[1]])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        arg = parse(line)
        if len(line) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.Class:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg[0]+"."+arg[1]not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[arg[0]+"."+arg[1]]
            storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
         based or not on the class name
         """
        arg = parse(line)
        objs = []
        if len(line) == 0:
            for val in storage.all().values():
                objs.append(str(val))
            print(objs)
        elif arg[0] in HBNBCommand.Class:
            for key, val in storage.all().items():
                if arg[0] in key:
                    objs.append(str(val))
            print(objs)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute
        """
        arg = parse(line)
        if len(line) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.Class:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg[0]+"."+arg[1]not in storage.all():
            print("** no instance found **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        else:
            for key, val in storage.all().items():
                if arg[0]+"."+arg[1] == key:
                    setattr(storage.all()[key], arg[2], arg[3])
                    storage.save()
                    break

    def count(self, line):
        """to retrieve the number of instances of a class"""
        if line in HBNBCommand.Class:
            i = 0
            for key, val in storage.all().items():
                if line in key:
                    i += 1
            print(i)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """default commands"""
        classt = []
        for i in line.split("."):
            classt.append(i)
        if len(classt) < 2:
            print("**Unknown syntax")
        else:
            rexp = re.sub("[\(\[].*?[\)\]]", "", classt[1])
            if rexp == "show":
                HBNBCommand.do_show(self, classt[0] + " " +
                                    classt[1][len(rexp)+2:-2])
            elif rexp == "destroy":
                HBNBCommand.do_destroy(self, classt[0] + " " +
                                       classt[1][len(rexp) + 2:-2])
            elif rexp == "all":
                HBNBCommand.do_all(self, classt[0] + " " + classt[1])
            elif rexp == "count":
                HBNBCommand.count(self, classt[0])
            else:
                print("***Unknown syntax")


def parse(line):
    """to parse users input"""
    return tuple(line.split())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
