#!/usr/bin/python3
"""
Module - Engine
"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """class FileStorage"""
    __file_path = "file.json"
    __objects = {}
    dict = {"BaseModel": BaseModel, "User": User, "State": State,
            "Amenity": Amenity, "City": City, "Place": Place, "Review": Review}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Adds new object"""
        if obj:
            i = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[i] = obj

    def save(self):
        j = {k: self.__objects[k].to_dict() for k in self.__objects.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(j, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                k = json.load(f)
                for key, val in k.items():
                    dict_objc = self.dict[val['__class__']](**val)
                    self.__objects[key] = dict_objc
