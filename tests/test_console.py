#!/usr/bin/python3
"""" Test file for Console"""

from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage
import unittest
import console
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """ Console Test cases"""
    """Check for docstring existance"""

    def test_docstrings_test1(self):
        """Test docstrings for console.py"""
        self.assertTrue(len(console.__doc__) >= 1)

    def test_docstrings_test2(self):
        """Test docstrings for test_console.py"""
        self.assertTrue(len(self.__doc__) >= 1)

    def test_docstrings_test3(self):
        """Test docstrings for console.py"""
        self.assertFalse(len(console.__doc__) < 1)

    def test_docstrings_test4(self):
        """Test docstrings for console.py"""
        self.assertFalse(len(self.__doc__) < 1)

    def test_class1(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Alx.count()"))

    def test_class2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Alx.all()"))

    def test_class3(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Base.show()"))

    def test_class4(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("A"))

    def test_show1(self):
        with patch("sys.stdout", new=StringIO()) as output:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("show"))
                self.assertEqual("** class name missing **", output.getvalue().strip())

    def test_show2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show ALX"))
            self.assertEqual("** class doesn't exist **", output.getvalue().strip())


    def test_show3(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Base"))
            self.assertEqual("** class doesn't exist **", output.getvalue().strip())

    def test_show4(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual("** instance id missing **", output.getvalue().strip())

    def test_all1(self):
        with patch("sys.stdout", new=StringIO()) as output:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("all Base"))
                self.assertEqual("** class doesn't exist **", output.getvalue().strip())

    def test_all2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Base2"))
            self.assertEqual("** class doesn't exist **", output.getvalue().strip())


    def test_all3(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Alx"))
            self.assertEqual("** class doesn't exist **", output.getvalue().strip())

    def test_update1(self):
        with patch("sys.stdout", new=StringIO()) as output:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("Update Base"))
                self.assertEqual("** class doesn't exist **", output.getvalue().strip())

    def test_update2(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Update BaseModel"))
            self.assertEqual("** instance id missing **", output.getvalue().strip())


    def test_update3(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 1234"))
            self.assertEqual("** no instance found **", output.getvalue().strip())

    def test_destroy_invalid_id_dot_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_all_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()