#!/usr/bin/python3
"""
Tests the Airbnb console
"""
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from console import HBNBCommand
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


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

    def test_emptyline(self):
        """ Tests that an emptyline is produced when the ENTER key
        is pressed
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_help(self):
        """ Tests the `help` command that displays help information about the
        available commands
        """
        r = r"Documented commands \(type help <topic>\):.*"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertRegex(f.getvalue(), r)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertRegex(f.getvalue(), "USAGE: show <class name> <id>")

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

    def test_all(self):
        """ Tests the <class name>.all() command that prints all the
        instances of the given class
        """
        b1 = BaseModel()
        r = "".join([r"\[BaseModel\]\s\([a-f\d]{8}-[a-f\d]{4}",
                     r"-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}\)\s\{.*\}"])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            self.assertRegex(f.getvalue(), r)

        r1 = Review()
        r = "".join([r"\[Review\]\s\([a-f\d]{8}-[a-f\d]{4}",
                     r"-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}\)\s\{.*\}"])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
            self.assertRegex(f.getvalue(), r)

        u1 = User()
        r = "".join([r"\[User\]\s\([a-f\d]{8}-[a-f\d]{4}",
                     r"-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}\)\s\{.*\}"])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            self.assertRegex(f.getvalue(), r)

        s1 = State()
        r = "".join([r"\[State\]\s\([a-f\d]{8}-[a-f\d]{4}",
                     r"-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}\)\s\{.*\}"])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
            self.assertRegex(f.getvalue(), r)

        c1 = City()
        r = "".join([r"\[City\]\s\([a-f\d]{8}-[a-f\d]{4}",
                     r"-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}\)\s\{.*\}"])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
            self.assertRegex(f.getvalue(), r)

        a1 = Amenity()
        r = "".join([r"\[Amenity\]\s\([a-f\d]{8}-[a-f\d]{4}",
                     r"-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}\)\s\{.*\}"])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
            self.assertRegex(f.getvalue(), r)

        p1 = Place()
        r = "".join([r"\[Place\]\s\([a-f\d]{8}-[a-f\d]{4}",
                     r"-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}\)\s\{.*\}"])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
            self.assertRegex(f.getvalue(), r)

    def test_count(self):
        """ Tests <class name>.count() command that prints the number of
        instances of a given class
        """
        b1 = BaseModel()
        b2 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual(f.getvalue(), '2\n')

        r1 = Review()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
            self.assertEqual(f.getvalue(), '1\n')

        u1 = User()
        u2 = User()
        u3 = User()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(f.getvalue(), '3\n')

        s1 = State()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
            self.assertEqual(f.getvalue(), '1\n')

        c1 = City()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
            self.assertEqual(f.getvalue(), '1\n')

        a1 = Amenity()
        a2 = Amenity()
        a3 = Amenity()
        a4 = Amenity()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual(f.getvalue(), '4\n')

        p1 = Place()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
            self.assertEqual(f.getvalue(), '1\n')

    def test_show(self):
        """ Test the <class name>.show() command that prints an instance
        """
        b1 = BaseModel()
        r = "".join([r"\[BaseModel\]\s\([a-f\d]{8}-[a-f\d]{4}",
                     r"-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}\)\s\{.*\}"])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show({b1.id})")
            self.assertRegex(f.getvalue(), r)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

        r1 = Review()
        r = "".join([r"\[Review\]\s\([a-f\d]{8}-[a-f\d]{4}",
                     r"-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}\)\s\{.*\}"])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show({r1.id})")
            self.assertRegex(f.getvalue(), r)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.show(fake_id)")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

        u1 = User()
        r = "".join([r"\[User\]\s\([a-f\d]{8}-[a-f\d]{4}",
                     r"-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}\)\s\{.*\}"])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show({u1.id})")
            self.assertRegex(f.getvalue(), r)

        s1 = State()
        r = "".join([r"\[State\]\s\([a-f\d]{8}-[a-f\d]{4}",
                     r"-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}\)\s\{.*\}"])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show({s1.id})")
            self.assertRegex(f.getvalue(), r)

        c1 = City()
        r = "".join([r"\[City\]\s\([a-f\d]{8}-[a-f\d]{4}",
                     r"-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}\)\s\{.*\}"])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.show({c1.id})")
            self.assertRegex(f.getvalue(), r)

        a1 = Amenity()
        r = "".join([r"\[Amenity\]\s\([a-f\d]{8}-[a-f\d]{4}",
                     r"-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}\)\s\{.*\}"])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show({a1.id})")
            self.assertRegex(f.getvalue(), r)

        p1 = Place()
        r = "".join([r"\[Place\]\s\([a-f\d]{8}-[a-f\d]{4}",
                     r"-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}\)\s\{.*\}"])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show({p1.id})")
            self.assertRegex(f.getvalue(), r)

    def test_destroy(self):
        """ Test the <class name>.destroy(id) command that deletes an instance
        of the given class
        """
        b1 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.destroy({b1.id})")
            self.assertEqual(f.getvalue(), "")
        with self.assertRaises(KeyError):
            print(storage.all()[f'BaseModel.{b1.id}'])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

        r1 = Review()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.destroy({r1.id})")
            self.assertEqual(f.getvalue(), "")
        with self.assertRaises(KeyError):
            print(storage.all()[f'Review.{r1.id}'])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.destroy(fake_id)")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

        u1 = User()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.destroy({u1.id})")
            self.assertEqual(f.getvalue(), "")
        with self.assertRaises(KeyError):
            print(storage.all()[f'User.{u1.id}'])

        s1 = State()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.destroy({s1.id})")
            self.assertEqual(f.getvalue(), "")
        with self.assertRaises(KeyError):
            print(storage.all()[f'State.{s1.id}'])

        c1 = City()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.destroy({c1.id})")
            self.assertEqual(f.getvalue(), "")
        with self.assertRaises(KeyError):
            print(storage.all()[f'City.{c1.id}'])

        a1 = Amenity()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.destroy({a1.id})")
            self.assertEqual(f.getvalue(), "")
        with self.assertRaises(KeyError):
            print(storage.all()[f'Amenity.{a1.id}'])

        p1 = Place()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.destroy({p1.id})")
            self.assertEqual(f.getvalue(), "")
        with self.assertRaises(KeyError):
            print(storage.all()[f'Place.{p1.id}'])
