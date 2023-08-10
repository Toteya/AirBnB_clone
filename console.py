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
        """ Prints a string representation of all instances based on the class
        name. If no class name is provided all instances of all classes are
        printed.
        """
        str_objs = []

        if class_name and class_name not in self.classes:
            print("** class doesn't exist **")
        else:
            for obj in models.storage.all().values():
                if not class_name or obj.__class__.__name__ == class_name:
                    str_objs.append(str(obj))
            print(str_objs)

    def help_all(self):
        help_str = "\n".join(["Prints a string representation of all "+
                              "instancesbased on the class",
                              "If no class name is provided all instances "+
                              "of all classes are printed."])
        print(help_str)


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
        help_str = "\n".join(["Creates a new instance of BaseModel, "+
                              "saves it to the file, and prints its id"])
        print(help_str)

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
        help_str = "Deletes an instance based on the class name and the id"
        print(help_str)

    def do_EOF(self, line):
        """Exits the programm
        """
        return True

    def help_EOF(self):
        help_str = "Exits the program"
        print(help_str)

    def do_quit(self, line):
        """Exits the programm
        """
        pass

    def help_quit(self):
        help_str = "Exits the program"
        print(help_str)

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
        help_str = "\n".join(['Prints the string reprensation of an instance '+
                              'based on the class name and the id',
                              'Usage: show <class name> <id>]'])
        print(help_str)

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or
        updating the attribute, and save the change to the file.
        """
        class_name = ""
        obj_id = ""
        attr_name = ""
        attr_value = ""

        args = line.split()
        try:
            class_name = args[0]
            obj_id = args[1]
            attr_name = args[2]
            attr_value = args[3]
        except IndexError:
            pass

        if not class_name:
            print("** class name missing **")
        elif class_name not in self.classes:
            print("** class doesn't exist **")
        elif not obj_id:
            print("** instance id missing **")
        elif f'{class_name}.{obj_id}' not in models.storage.all():
            print("** no instance found **")
        elif not attr_name:
            print("** attribute name missing **")
        elif not attr_value:
            print("** value missing **")
        else:
            obj = models.storage.all()[f'{class_name}.{obj_id}']
            if hasattr(obj, attr_name):
                setattr(obj, attr_name, attr_value)

    def help_update(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
