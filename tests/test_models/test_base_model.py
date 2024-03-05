#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
import datetime as dt

class TestBaseModel(unittest.TestCase):
    def test_attr(self):
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_id_diff(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at(self):
        model = BaseModel()
        self.assertIsInstance(model.created_at, dt.datetime)

    def test_updated_at(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_str_rep(self):
        model = BaseModel()
        expected_output = f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_output)

if __name__ == '__main__':
    unittest.main()
