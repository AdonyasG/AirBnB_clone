#!/usr/bin/python3
""" Test Case For class and methods """
import unittest
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models import storage
from datetime import datetime
from models.review import Review
import pep8


class TestReview(unittest.TestCase):
    """ UnitTest for class Review"""
    def test_equal(self):
        """ check for attributes have correclty assigned"""
        review = Review()
        review.place_id = "Addis-12345"
        self.assertEqual(review.place_id, "Addis-12345")
        self.assertIsNotNone(Review().text)

    def test_attr(self):
        """checcking for attribute present in the Review Class"""
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertTrue(hasattr(review, "place_id"))
        self.assertFalse(hasattr(review, "age"))

    def test_type(self):
        """check type of Review"""
        self.assertTrue(str, type(Review().text))
        self.assertTrue(str, type(Review().place_id))

    def testdatetype(self):
        """test type of date """
        self.assertEqual(datetime, type(Review().created_at))
        self.assertEqual(datetime, type(Review().updated_at))

    def test_classfound(self):
        """ class found in __object"""
        self.assertIn(Review(), storage.all().values())

    def test_instancedifferent(self):
        """check for instance different"""
        city1 = Review()
        city2 = Review()
        self.assertNotEqual(city1, city2)
        self.assertIsInstance(city1, type(Review()))
        self.assertIsInstance(city2, type(Review()))

    def testisnotint(self):
        review = City()
        self.assertNotIsInstance(review, type(Review()))

    def test_save(self):
        """ check for created_at and update_at"""
        City.save(self)
        self.assertNotEqual(Review().created_at, Review().updated_at)

    def test_subclass(self):
        """ checking for issubclass"""
        self.assertTrue(issubclass(Review().__class__, BaseModel), True)

    def test_date_interval_increated(self):
        """ created date interval checking"""
        user1 = Review()
        user2 = Review()
        self.assertLess(user1.created_at, user2.created_at)

    def test_date_interval_in_updated(self):
        """updated date interval checking"""
        city1 = Review()
        city2 = Review()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_in_dict(self):
        """checking in dict function"""
        city = Review()
        city.my_address = "4r4622"
        self.assertIn("my_address", city.to_dict())

    def test_id_different(self):
        """ checking id defference """
        city1 = Review()
        city2 = Review()
        self.assertNotEqual(city1.id, city2.id)


if __name__ == '__main__':
    unittest.main()
