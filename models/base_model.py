#!/usr/bin/python3

import uuid
import datetime as d
import models


class BaseModel:
    """Defines all common attributes of other classes"""


    def __init__(self, *args, **kwargs):
        """Public instance attributes"""

        self.id = str(uuid.uuid4())
        self.created_at = d.datetime.now()
        self.updated_at = d.datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = d.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """String representation of the class BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute - updated_at """
        self.updated_at = d.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary that contains all key/values in the instance's dict"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        
        if isinstance(my_dict["created_at"], d.datetime):
            my_dict["created_at"] = my_dict["created_at"].isoformat()
        if isinstance(my_dict["updated_at"], d.datetime):
            my_dict["updated_at"] = my_dict["updated_at"].isoformat()

        return my_dict
