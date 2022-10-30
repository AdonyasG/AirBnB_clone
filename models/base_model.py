#!/usr/bin/python3
"""
Module - Base
"""
import models
import uuid
from datetime import datetime


class BaseModel():
    """class BaseModel"""
    def __init__(self, *args, **kwargs):
        """initialize"""
        if kwargs:
            for k, v in kwargs.items():
                if "created_at" == k:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == k:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == k:
                    pass
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        return ('[{}] ({}) {}'.format(
               self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        i = self.__dict__.copy()
        i["created_at"] = self.created_at.isoformat()
        i["updated_at"] = self.updated_at.isoformat()
        i["__class__"] = self.__class__.__name__
        return i
