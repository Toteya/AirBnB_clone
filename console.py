#!/usr/bin/python3
"""
console module
A console / command interpreter program for an Airbnb clone
Entry point to the program
"""
import cmd
import sys
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    A command interpreter for an Airbnb clone
    """

    prompt = '(hbnb) '
    classes = ['BaseModel']

    def do_all(self, class_name):
        """ Prints string representations of all instances based on the class
        name. If no class name is provided all instances of all classes are
        printed.
        """
        if not class_name:
            for obj in models.storage.all().values():
                print(obj)
        elif class_name in self.classes:
            for obj in models.storage.all().values():
                if obj.__class__.__name__ == class_name:
                    print(obj)
        else:
            print("** class doesn't exist **")

    def help_all(self):
        pass


    def do_create(self, class_name):
        """ Creates a new instance of BaseModel, saves it the file,
        and prints its id
        """
        if not class_name:
            print("** class name missing **")
        elif class_name not in self.classes:
            print("** class doesn't exist **")
        else:
            bm = BaseModel()
            bm.save()
            print(bm.id)

    def help_create(self):
        pass

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and the id
        """
        class_name = ""
        obj_id = ""

        args = line.split()
        if args:
            class_name = args[0]
        if len(args) > 1:
            obj_id = args[1]

        if not class_name:
            print("** class name missing **")
        elif class_name not in self.classes:
            print("** class doesn't exist **")
        elif not obj_id:
            print("** instance id missing **")
        elif f'{class_name}.{obj_id}' not in models.storage.all():
            print("** no instance found **")
        else:
            obj = models.storage.all()[f'{class_name}.{obj_id}']
            del models.storage.all()[f'{class_name}.{obj_id}']
            del obj
            models.storage.save()

    def help_destroy():
        pass

    def do_EOF(self, line):
        """Exits the programm
        """
        return True

    def help_EOF(self):
        pass

    def do_quit(self, line):
        """Exits the programm
        """
        pass

    def help_quit(self):
        pass

    def do_show(self, line):
        """ Prints the string representation of an instance based on the
        class name and the id
        """
        class_name = ""
        obj_id = ""

        args = line.split()
        if args:
            class_name = args[0]
        if len(args) > 1:
            obj_id = args[1]

        if not class_name:
            print("** class name missing **")
        elif class_name not in self.classes:
            print("** class doesn't exist **")
        elif not obj_id:
            print("** instance id missing **")
        elif f'{class_name}.{obj_id}' not in models.storage.all():
            print("** no instance found **")
        else:
            obj = models.storage.all()[f'{class_name}.{obj_id}']
            print(obj)

    def help_show(self):
        pass

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or
        updating the attribute, and save the change to the file.
        """
        pass

    def help_update(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
