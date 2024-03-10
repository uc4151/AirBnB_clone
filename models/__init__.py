#!/usr/bin/python3
"""Initilizing models as a package"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
