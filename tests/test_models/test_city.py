#!/usr/bin/python3
""" Test Case For class and methods """
import unittest
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models import storage
from datetime import datetime
import pep8


class TestCity(unittest.TestCase):
    """ UnitTest for class City"""
    def test_equal(self):
        """ check for attributes have correclty assigned"""
        city = City()
        city.state_id = "Addis-12345"
        city.name = "Addis Ababa"
        self.assertEqual(city.state_id, "Addis-12345")
        self.assertEqual(city.name, "Addis Ababa")
        self.assertIsNotNone(City().name)

    def test_attr(self):
        """checcking for attribute present in the City Class"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "state_id"))
        self.assertFalse(hasattr(city, "age"))
    def test_type(self):
        """check type of class"""
        self.assertTrue(str, type(City().name))
        self.assertTrue(str, type(City().state_id))
        self.assertEqual(datetime, type(City().created_at))
        self.assertEqual(datetime, type(City().updated_at))

    def test_classfound(self):
        """ class found in __object"""
        self.assertIn(City(), storage.all().values())

    def test_instancedifferent(self):
        """check for instance different"""
        city1 = City()
        city2 = City()
        city3 = User()
        self.assertNotEqual(city1, city2)
        self.assertIsInstance(city1, type(City()))
        self.assertIsInstance(city2, type(City()))
        self.assertNotIsInstance(city3, type(City()))

    def test_save(self):
        """ check for created_at and update_at"""
        City.save(self)
        self.assertNotEqual(City().created_at, City().updated_at)

    def test_subclass(self):
        """ checking for issubclass"""
        self.assertTrue(issubclass(City().__class__, BaseModel), True)
    def test_date_interval_increated(self):
        """ created date interval checking"""
        user1 = City()
        user2 = City()
        self.assertLess(user1.created_at,user2.created_at)

    def test_date_interval_in_updated(self):
        """updated date interval checking"""
        city1 = City()
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_in_dict(self):
        """checking in dict function"""
        city = City()
        city.my_address = "4r4622"
        self.assertIn("my_address", city.to_dict())

    def test_id_different(self):
        """ checking id defference """
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)


if __name__ == '__main__':
    unittest.main()