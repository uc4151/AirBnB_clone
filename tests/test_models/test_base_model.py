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
        expected_output = "[{}] ({}) {}".format(model.__class__.__name__, model.id, model.__dict__)
        self.assertEqual(str(model), expected_output)

    def test_to_dict_rep(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_with_instance(self):
        created_at = '2022-01-01T12:00:00.000000'
        updated_at = '2022-01-01T12:30:00.000000'
        model = BaseModel(created_at=created_at, updated_at=updated_at)
        self.assertEqual(model.created_at, dt.datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(model.updated_at, dt.datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S.%f'))

if __name__ == '__main__':
    unittest.main()
