#!/usr/bin/python3
""" Test Case for File Storage """

import unittest
import models
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.user import User
import pep8


class TestFileStorage(unittest.TestCase):
    """ Test case for """

    def test_style_check(self):
        """ Tests pep8 style """
        style = pep8.StyleGuide(quiet=True)
        pep_8 = style.check_files(['models/file_storage.py'])
        self.assertEqual(pep_8.total_errors, 0, "Fix and update your user.py file")

    def test_all(self):
        """ test case for all method """
        self.assertTrue(type(storage.all()), dict)

    def test_all2(self):
        """ test case2 for all method """
        self.assertIsNotNone(storage.all())

    def test_new(self):
        """test file new method"""
        self.assertIn("BaseModel." + BaseModel().id, models.storage.all().keys())

    def test_new2(self):
        """ Test new method """
        self.assertIn("User." + User().id, models.storage.all().keys())

    def test_new3(self):
        """Test new method"""
        self.assertIn("City." + City().id, models.storage.all().keys())
        self.assertIsNot("AbdiOlana." + User().id, models.storage.all().keys())


if __name__ == '__main__':
    unittest.main()
