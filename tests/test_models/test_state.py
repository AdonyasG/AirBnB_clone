#!/usr/bin/python3
""" Test Case For class and methods """
import unittest
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models import storage
from datetime import datetime



class TestCity(unittest.TestCase):
    """ UnitTest for class City"""
    def test_equal(self):
        """ check for attributes have correclty assigned"""
        state = State()
        state.name = "Addis Ababa"
        self.assertEqual(state.name,"Addis Ababa")
        self.assertIsNotNone(City().name)

    def test_attr(self):
        """checcking for attribute present in the City Class"""
        state = State()
        city = City()
        self.assertTrue(hasattr(state, "name"))
        self.assertFalse(hasattr(city, "age"))
    def test_type(self):
        """check type of class"""
        self.assertTrue(str, type(State().name))
        self.assertEqual(datetime, type(State().created_at))
        self.assertEqual(datetime, type(State().updated_at))

    def test_classfound(self):
        """ class found in __object"""
        self.assertIn(State(), storage.all().values())

    def test_instancedifferent(self):
        """check for instance different"""
        state1 = State()
        state2 = State()
        state3 = City()
        self.assertNotEqual(state2, state1)
        self.assertIsInstance(state1, type(State()))
        self.assertIsInstance(state2, type(State()))
        self.assertNotIsInstance(state3, type(State()))

    def test_save(self):
        """ check for created_at and update_at"""
        State.save(self)
        self.assertNotEqual(State().created_at, State().updated_at)

    def test_subclass(self):
        """ checking for issubclass"""
        self.assertTrue(issubclass(State().__class__, BaseModel), True)
    def test_date_interval_increated(self):
        """ created date interval checking"""
        state1 = State()
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)

    def test_date_interval_in_updated(self):
        """updated date interval checking"""
        state1 = State()
        state2 = State()
        self.assertLess(state1.updated_at, state2.updated_at)

    def test_in_dict(self):
        """checking in dict function"""
        city = State()
        city.my_address = "4r4622"
        self.assertIn("my_address", city.to_dict())

    def test_id_different(self):
        """ checking id defference """
        city1 = State()
        city2 = State()
        self.assertNotEqual(city1.id, city2.id)

    def test_checking_for_functions(self):
        self.assertIsNotNone(State.__doc__)

    def test_style_check(self):
        """ Tests pep8 style """
        style = pep8.StyleGuide(quiet=True)
        pep_8 = style.check_files(['models/user.py'])
        self.assertEqual(pep_8.total_errors, 0, "Fix and update your user.py file")

    def test_is_subclass(self):
        state = State()
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)


if __name__ == '__main__':
    unittest.main()