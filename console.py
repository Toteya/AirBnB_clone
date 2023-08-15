#!/usr/bin/python3
"""
console module
A console / command interpreter program for an Airbnb clone
Entry point to the program
"""
import cmd
import re
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    A command interpreter for an Airbnb clone HBNBCommand class
    """

    prompt = '(hbnb) '
    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }

    def default(self, line):
        """Handles commands that do not match any of the defined methods
        """
        match_cmd = re.match(r"(^\w+)\.(\w+)\((.*)\)$", line)

        if match_cmd:
            class_name = match_cmd.group(1)
            method = match_cmd.group(2)
            args = match_cmd.group(3)
            if class_name in self.classes and hasattr(self, f'do_{method}'):
                self._precmd(method, class_name, args)
                return
        super().default(line)

    def _precmd(self, method, class_name, args):
        """ Executes a command based on the given method, class_name
        and arguments
        """

        if method == 'update' and re.search(r"\{.*\}", args):
            split_args = re.split(r'{|}|,|:', args)

            # args = [arg for arg in split_args if arg.strip()] USE THIS CODE!

            args = []
            for arg in split_args:
                if not all(ch == ' ' for ch in arg):
                    args.append(arg.strip())

            for i in range(1, len(args), 2):
                str = args[0]
                try:
                    str += " " + args[i]
                except IndexError:
                    pass
                try:
                    str += " " + args[i + 1]
                except IndexError:
                    pass
                self.onecmd(f"{method} {class_name} {str}")
        else:
            args = "".join(re.split(r'{|}|,|:', args))
            self.onecmd(f"{method} {class_name} {args}")

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
        """Prints command help info"""
        help_str = "\n".join(['USAGE: all [<class name>]',
                              'Prints a string representation of all ' +
                              'instances based on the class name',
                              'If no class name is provided all instances ' +
                              'of all classes are printed.'])
        print(help_str)

    def do_create(self, class_name):
        """ Creates a new instance of the given class, saves it the file,
        and prints its id
        """
        if not class_name:
            print("** class name missing **")
        elif class_name not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = self.classes[class_name]()
            obj.save()
            print(obj.id)

    def help_create(self):
        """Prints command help info"""
        help_str = "\n".join(["USAGE: create <class name>",
                              "Creates a new instance of BaseModel, " +
                              "saves it to the file, and prints its id"])
        print(help_str)

    def do_count(self, class_name):
        """ Prints the number of instances of the given class
        """
        number_objs = 0
        if not class_name:
            print("** class name missing **")
        elif class_name not in self.classes:
            print("** class doesn't exist **")
        else:
            for obj in models.storage.all().values():
                if obj.__class__.__name__ == class_name:
                    number_objs += 1
            print(number_objs)

    def help_count(self):
        """Prints command help info"""
        help_str = "Prints the number of instances for a given class"
        print(help_str)

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and the id
        """
        class_name = ""
        obj_id = ""

        args = line.split()
        try:
            class_name = args[0]
            obj_id = args[1]
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
        else:
            obj = models.storage.all()[f'{class_name}.{obj_id}']
            del models.storage.all()[f'{class_name}.{obj_id}']
            del obj
            models.storage.save()

    def help_destroy(self):
        """Prints command help info"""
        help_str = "\n".join(["USAGE: destroy <class name> <id>",
                              "Deletes an instance based on the class name " +
                              "and the id"])
        print(help_str)

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_EOF(self, line):
        """Exits the programm
        """
        print()
        return True

    def help_EOF(self):
        """Prints command help info"""
        help_str = "Exits the program"
        print(help_str)

    def do_quit(self, line):
        """Exits the programm
        """
        return True

    def help_quit(self):
        """Prints command help info"""
        help_str = "Exits the program"
        print(help_str)

    def do_show(self, line):
        """ Prints the string representation of an instance based on the
        class name and the id
        """
        class_name = ""
        obj_id = ""

        args = line.split()
        try:
            class_name = args[0]
            obj_id = args[1]
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
        else:
            obj = models.storage.all()[f'{class_name}.{obj_id}']
            print(obj)

    def help_show(self):
        """Prints command help info"""
        help_str = "\n".join(["USAGE: show <class name> <id>",
                              "Prints the string reprensation of an instance" +
                              " based on the class name and the id"])
        print(help_str)

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or
        updating the attribute, and save the change to the file.
        """
        class_name = ""
        obj_id = ""
        attr_name = ""
        attr_value = ""

        # line = line.split('"')
        # args = line[0].split()
        # args.extend(line[1:])
        args = self.parse_line(line)
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
            # cast attribute value to either an int, float or str
            if hasattr(obj, attr_name):
                a_type = type(getattr(obj, attr_name))
                setattr(obj, attr_name, a_type(attr_value))
            elif attr_value.isnumeric():
                setattr(obj, attr_name, int(attr_value))
            elif len(attr_value.split('.')) == 2:
                if all(part.isnumeric() for part in attr_value.split('.')):
                    setattr(obj, attr_name, float(attr_value))
            else:
                setattr(obj, attr_name, attr_value)
            obj.save()

    def help_update(self):
        """Prints command help info"""
        help_str = "\n".join(['USAGE: update <class name> <id> ' +
                              '<attribute name> "<attribute value>"',
                              'Updates an instance based on the class name ' +
                              'and id by adding or updating the attribute, ',
                              'and saves the change to the file.'])
        print(help_str)

    def parse_line(self, line):
        """ Converts a string into a list of arguments.
        Sub-strings in quotes are preserved as one argument
        """
        split_line = re.split(r'\'|"', line)
        args = []
        for arg in split_line:
            if arg and not all(c == ' ' for c in arg):
                args.append(arg.strip())

        args_list = []
        try:
            args_list = args[0].split()
            args_list.extend(args[1:])
        except IndexError:
            pass
        return args_list


if __name__ == '__main__':
    HBNBCommand().cmdloop()
