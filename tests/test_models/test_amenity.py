#!/usr/bin/python3
""" Test Case For class and methods """


import unittest
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models import storage
from datetime import datetime
from models.amenity import Amenity



class TestAmenity(unittest.TestCase):
    """ UnitTest for class Amenity"""
    def test_equal(self):
        """ check for attributes have correclty assigned"""
        a = Amenity()
        a.place_id = "Addis-12345"
        self.assertEqual(a.place_id, "Addis-12345")
        self.assertIsNotNone(Amenity().name)

    def test_attr(self):
        """checking for attribute present in the Amenity Class"""

        self.assertTrue(hasattr(Amenity, "name"))
        self.assertFalse(hasattr(Amenity, "age"))

    def test_type(self):
        """check type of Amenity"""
        self.assertTrue(str, type(Amenity().name))
        self.assertEqual(datetime, type(Amenity().created_at))
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_classfound(self):
        """ class found in __object"""
        self.assertIn(Amenity(), storage.all().values())

    def test_instancedifferent(self):
        """check for instance different"""
        city1 = Amenity()
        city2 = Amenity()
        city3 = User()
        self.assertNotEqual(city1, city2)
        self.assertIsInstance(city1, type(Amenity()))
        self.assertIsInstance(city2, type(Amenity()))

    def testisnotinstance(self):
        """" isnot instance """
        city3 = City()
        self.assertNotIsInstance(city3, type(Amenity()))

    def test_save(self):
        """ check for created_at and update_at"""
        City.save(self)
        self.assertNotEqual(Amenity().created_at, Amenity().updated_at)

    def testdatetype(self):
        """test type of date """
        self.assertEqual(datetime, type(Amenity().created_at))
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_subclass(self):
        """ checking for issubclass"""
        self.assertTrue(issubclass(Amenity().__class__, BaseModel), True)

    def test_date_interval_increated(self):
        """ created date interval checking"""
        user1 = Amenity()
        user2 = Amenity()
        self.assertLess(user1.created_at, user2.created_at)

    def test_date_interval_in_updated(self):
        """updated date interval checking"""
        city1 = Amenity()
        city2 = Amenity()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_in_dict(self):
        """checking in dict function"""
        city = Amenity()
        city.my_address = "4r4622"
        self.assertIn("my_address", city.to_dict())

    def test_id_different(self):
        """ checking id defference """
        city1 = Amenity()
        city2 = Amenity()
        self.assertNotEqual(city1.id, city2.id)


if __name__ == '__main__':
    unittest.main()
