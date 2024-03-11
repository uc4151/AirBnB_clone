#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
    Unittest classes:
        TestFileStorage
"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
     """Unittests for testing the FileStorage class."""

    def setUp(self):
        self.file_path = "test_file.json"
        self.file_storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        self.assertEqual(self.file_storage.all(), {})

    def test_new_and_save(self):
        obj = BaseModel()
        self.file_storage.new(obj)
        self.file_storage.save()
        with open(self.file_path, "r") as file_data:
            saved_data = json.load(file_data)
        expected_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(expected_key, saved_data)

    def test_reload(self):
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        with open(self.file_path, "w") as file_data:
            json.dump({key: obj.to_dict()}, file_data)
        self.file_storage.reload()
        self.assertIn(key, self.file_storage.all())

if __name__ == "__main__":
    unittest.main()
