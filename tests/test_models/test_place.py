#!/usr/bin/python3
""" Test Case For class and methods """
import unittest
import time
from models.base_model import BaseModel
from models.place import Place

from models import storage
from datetime import datetime



class TestPlace(unittest.TestCase):
    """ UnitTest for  class Place"""
    def test_equal(self):
        """ check for  a ttributes  have correclty assigned"""
        place = Place()
        place.name = "Alx"
        place.state_id = "alx@gmail.com"
        self.assertEqual(place.name, "Alx")
        self.assertEqual(place.state_id, "alx@gmail.com")
        self.assertNotEqual(place.name, "12345")
        self.assertEqual(place.name, "Alx")
        self.assertIsNotNone(place.state_id)

    def test_attr(self):
        """checcking for attribute present in the Place Class"""
        place = Place()
        self.assertTrue(hasattr(place,"name"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "name"))
        self.assertFalse(hasattr(place, "state_id"))
    def test_type(self):
        """check type of class"""
        self.assertTrue(str, type(Place().name))
        self.assertTrue(str, type(Place().name))
        self.assertTrue(str, type(Place().name))
        self.assertEqual(datetime, type(Place().created_at))
        self.assertEqual(datetime, type(Place().updated_at))

    def test_classfound(self):
        """ class found in __object"""
        self.assertIn(Place(),storage.all().values())

    def test_instancedifferent(self):
        """check for instance different"""
        place1 = Place()
        place2 = Place()
        place3 = Place()
        self.assertNotEqual(place1, place2)
        self.assertIsInstance(place1, type(Place()))
        self.assertIsInstance(place2, type(Place()))


    def test_subclass(self):
        """ checking for issubclass"""
        self.assertTrue(issubclass(Place().__class__, BaseModel), True)

    def test_date_interval_increated(self):
        """ created date interval checking"""
        place1 = Place()
        place2 = Place()
        self.assertLess(place1.created_at, place2.created_at)

    def test_date_interval_in_updated(self):
        """updated date interval checking"""
        city1 = Place()
        city2 = Place()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_in_dict(self):
        """checking in dict function"""
        place = Place()
        place.my_address = "4r4622"
        self.assertIn("my_address", place.to_dict())

    def test_id_different(self):
        """ checking id defference """
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)


if __name__ == '__main__':
    unittest.main()