#!/usr/bin/python3
""" Test Case For class and methods """


import unittest
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models import storage
from datetime import datetime
import pep8


class TestUser(unittest.TestCase):
    """ UnitTest for class User"""
    def test_equal(self):
        """ check for attributes have correclty assigned"""
        user  = User()
        user.first_name = "Alx"
        user.email = "alx@gmail.com"
        user.password = 12345
        user.last_name = "student"
        self.assertEqual(user.first_name,"Alx")
        self.assertEqual(user.email,"alx@gmail.com")
        self.assertNotEqual(user.password,"12345")
        self.assertEqual(user.last_name,"student")
        self.assertIsNotNone(User().email)

    def test_attr(self):
        """checcking for attribute present in the User Class"""
        user = User()
        self.assertTrue(hasattr(user,"first_name"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "last_name"))
        self.assertTrue(hasattr(user, "email"))
        self.assertFalse(hasattr(user, "age"))
    def test_type(self):
        """check type of class"""
        self.assertTrue(str, type(User().last_name))
        self.assertTrue(str, type(User().first_name))
        self.assertTrue(str, type(User().password))
        self.assertTrue(str, type(User().email))
        self.assertEqual(datetime, type(User().created_at))
        self.assertEqual(datetime, type(User().updated_at))

    def test_classfound(self):
        """ class found in __object"""
        self.assertIn(User(), storage.all().values())

    def test_instancedifferent(self):
        """check for instance different"""
        user1 = User()
        user2 = User()
        user3 = City()
        self.assertNotEqual(user1, user2)
        self.assertIsInstance(user1, type(User()))
        self.assertIsInstance(user2, type(User()))
        self.assertNotIsInstance(user3, type(User()))

    def test_save(self):
        """ check for created_at and update_at"""
        User.save(self)
        self.assertNotEqual(User().created_at, User().updated_at)

    def test_subclass(self):
        """ checking for issubclass"""
        self.assertTrue(issubclass(User().__class__, BaseModel), True)
    def test_date_interval_increated(self):
        """ created date interval checking"""
        user1 = User()
        user2 = User()
        self.assertLess(user1.created_at,user2.created_at)

    def test_date_interval_in_updated(self):
        """updated date interval checking"""
        user1 = User()
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_in_dict(self):
        """checking in dict function"""
        user = User()
        user.my_address = "4r4622"
        self.assertIn("my_address", user.to_dict())

    def test_id_different(self):
        """ checking id defference """
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_style_check(self):
        """ Tests pep8 style """
        style = pep8.StyleGuide(quiet=True)
        pep_8 = style.check_files(['models/user.py'])
        self.assertEqual(pep_8.total_errors, 0, "Fix and update your user.py file")

if __name__ == '__main__':
    unittest.main()