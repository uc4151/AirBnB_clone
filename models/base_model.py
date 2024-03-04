#!/usr/bin/python3

import uuid
import datetime as d

class BaseModel:
    """Defines all common attributes of other classes"""


    def __init__(self):
        """Public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = d.datetime.now()
        self.updated_at = d.datetime.now()


    def __str__(self):
        """String representation of the class BaseModel"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


    def save(self):
        """Update the public instance attribute - updated_at """
        self.updated_at = d.datetime.now()


    def to_dict(self):
        """Returns a dictionary that contains all key/values in the instance's dict"""
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict