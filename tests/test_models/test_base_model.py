import unittest
import time
import datetime
import pep8
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Tests base model class"""

    def test_uuid(self):
        """Test uuid attribute of class"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

    def test_created_at(self):
        """Test created_at attribute of class"""
        bm1 = BaseModel()
        time.sleep(0.1)
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertNotEqual(bm1.created_at, bm2.created_at)
        self.assertIsInstance(bm1.created_at, datetime.datetime)

    def test_updated_at(self):
        """Test updated_at attribute of class"""
        bm1 = BaseModel()
        time.sleep(0.1)
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "updated_at"))
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)
        self.assertIsInstance(bm1.updated_at, datetime.datetime)

    def test_typecheck(self):
        """checking type"""
        bm = BaseModel()
        self.assertTrue(bm, type(BaseModel))

    def test_typeof_attr(self):
        """test attributes type"""
        self.assertTrue(str, type(BaseModel().id))

    def test_style_check(self):
        """ Tests pep8 style """
        style = pep8.StyleGuide(quiet=True)
        pep_8 = style.check_files(['models/user.py'])
        self.assertEqual(pep_8.total_errors, 0, "Fix and update your user.py file")

    def test_class_found(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_str_id(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_datetime_created(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_datetime_update(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_different(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)


if __name__ == '__main__':
    unittest.main()
