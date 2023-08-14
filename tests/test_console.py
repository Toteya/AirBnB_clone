#!/usr/bin/python3
"""
Tests the Airbnb console
"""
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class TestHBNBCommand(TestCase):
    """
    Tests the HBNBCommand class from the console
    module
    """

    def setUp(self):
        """ Sets up the initial conditions of each test
        """
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tears down the testing conditions after each test
        """
        FileStorage._FileStorage__objects = {}

    def default(self):
        """ Tests the default method that handles commands that are not
        defined in the 'do_methods'
        """

    def test_do_all(self):
        """ Tests the `all` command that prints a string respresentation of
        all the instances
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual(f.getvalue(), "[]\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        b1 = BaseModel()
        exp_out = f'["{str(b1)}"]\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual(f.getvalue(), exp_out)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertEqual(f.getvalue(), exp_out)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertEqual(f.getvalue(), "[]\n")

    def test_do_create(self):
        """ Tests the `create` command that creates
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create FakeClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        r = r"^[a-f\d]{8}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertRegex(f.getvalue(), r)

    def test_do_count(self):
        """ Tests the `count` command that prints the number of instances
        of a given class
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count FakeClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
            self.assertEqual(f.getvalue(), "0\n")

        b1 = BaseModel()
        b2 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
            self.assertEqual(f.getvalue(), "2\n")

    def test_do_destroy(self):
        """ Tests the `destroy` command that deletes an instance
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy FakeClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User fake_id")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

        user1 = User()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {user1.id}")
            self.assertEqual(f.getvalue(), "")

    def test_do_EOF(self):
        """ Tests the `EOF` command that exits the console
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "\n")

    def test_do_quit(self):
        """ Tests the `quit` command that exits the console
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

    def test_do_show(self):
        """ Tests the `show` command that prints a given instance
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show FakeClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User fake_id")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

        user1 = User()
        # regex pattern for User.id
        r = "".join([r"^\[User\]\s\([a-f\d]{8}-[a-f\d]{4}",
                     r"-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}\)\s\{.*\}"])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user1.id}")
            self.assertRegex(f.getvalue(), r)

    def test_do_update(self):
        """ Tests the `update` command that updates the attributes of an
        instance
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update FakeClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User fake_id")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

        user1 = User()
        created = user1.created_at
        updated = user1.updated_at
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {user1.id}")
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {user1.id} 'name'")
            self.assertEqual(f.getvalue(), "** value missing **\n")

        self.assertEqual(user1.first_name, "")
        self.assertNotIn('first_name', str(user1))
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = "".join([f"update User {user1.id} ",
                           "'first_name' \"Ronaldo\""])
            HBNBCommand().onecmd(cmd)
            self.assertEqual(f.getvalue(), "")
        self.assertEqual(user1.first_name, "Ronaldo")

        with self.assertRaises(AttributeError):
            print(user1.nick_name)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update User {user1.id} "nick_name" "R9"')
            self.assertEqual(f.getvalue(), "")
        self.assertEqual(user1.nick_name, "R9")

        self.assertEqual(user1.email, "")
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = "".join([f'update User {user1.id} ',
                           'email "r9@goalmachine.com" ',
                           '"nick_name" "fenomeno"'])
            HBNBCommand().onecmd(cmd)
            self.assertEqual(f.getvalue(), "")
        self.assertEqual(user1.email, "r9@goalmachine.com")
        self.assertEqual(user1.nick_name, "R9")

        self.assertNotIn('last_name', str(user1))
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = "".join([f'update User {user1.id} ',
                           '"last_name" \'Nazario de Lima\''])
            HBNBCommand().onecmd(cmd)
            self.assertEqual(f.getvalue(), "")
        self.assertEqual(user1.last_name, "Nazario de Lima")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update User {user1.id} age "32"')
            self.assertEqual(f.getvalue(), "")
        self.assertIsInstance(user1.age, int)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update User {user1.id} height "1.83"')
            self.assertEqual(f.getvalue(), "")
        self.assertIsInstance(user1.height, float)
        self.assertNotEqual(user1.updated_at, updated)
        self.assertGreater(user1.updated_at, created)
