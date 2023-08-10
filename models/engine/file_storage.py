#!/usr/bin/python3
"""Module for FileStorage class."""
import os
import json
import datetime


class FileStorage:

    """Class for serializtion and deserialization of base classes."""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """init method for FileStorage class
        """
        pass

    def all(self):
        """Returns __objects dictionary"""
        return type(self).__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """Serialzes __objects to JSON file."""
        dictionary = dict()
        for k, v in type(self).__objects.items():
            dictionary[k] = v.to_dict()
        with open(type(self).__file_path, 'w', encoding='utf-8') as my_file:
            json.dump(dictionary, my_file)

    def reload(self):
        """Deserializes JSON file into __objects."""
        try:
            with open(type(self).__file_path, 'r', encoding='utf-8') as j_file:
                json_load = json.load(my_file)
            for k, v in json_load.items():
                FileStorage.__objects[k] = BaseModel(**v)
        except json.JSONDecodeError:
            pass
        except FileNotFoundError:
            pass
