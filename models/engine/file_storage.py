#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:
    """This class serializes instances to a JSON file 
        and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """This method returns all objects in the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Creates new object with the key: 'class_name.id'"""
        obj_className = obj.__class__.__name__
        key = "{}.{}".format(obj_className, obj.id)
        FileStorage.__objects[key] = obj


    def save(self):
        """This method serializes available dictionary 
        and stores them in a json file
        """
        file_dict = FileStorage.__objects
        obj_dict = {obj: file_dict[obj].to_dict() for obj in file_dict.keys()}

        with open(FileStorage.__file_path, "w") as file_data:
            json.dump(obj_dict, file_data, indent=4)
            file_data.write("\n")


    def reload(self):
        """This method deserializes JSON file to __objects if the file 
            exists; otherwise, do nothing
        """
        try:
            with open(FileStorage.__file_path, "r") as file_data:
                FileStorage.__objects = json.load(file_data)
                for obj in FileStorage.__objects.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except ValueError:
                            print("Error: Invalid JSON data in file.")
        except FileNotFoundError:
            pass
    try:
        with open(FileStorage.__file_path, "r") as file_data:
            try:
                FileStorage.__objects = json.load(file_data)
                for obj in FileStorage.__objects.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
            except ValueError:
                print("Error: Invalid JSON data in file.")                                                                                                          
    except FileNotFoundError:
        pass
