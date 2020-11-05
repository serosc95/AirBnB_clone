#!/usr/bin/python3
"""Module for class BaseModel
"""
import uuid
import datetime
import models


class BaseModel():
    """Class BaseModel, this class make
    or created the instances and the
    assign various atributes principal
    that should tener each object
    """

    def __init__(self, *args, **kwargs):
        """ initializes each instance of BaseModel Class
        """
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
                if k == "created_at" or k == "updated_at":
                    form = '%Y-%m-%dT%H:%M:%S.%f'
                    setattr(self, k, datetime.datetime.strptime(v, form))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ return a string with the atributes
        of the instance
        """
        name = type(self).__name__
        dic = self.__dict__
        return "[{}] ({}) {}".format(name, self.id, dic)

    def save(self):
        """update the date of the atribute update
        and the store
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return a dict with all
        keys/values of the instance
        """
        dicts = self.__dict__.copy()
        dicts["created_at"] = self.created_at.isoformat()
        dicts["updated_at"] = self.updated_at.isoformat()
        dicts["__class__"] = type(self).__name__
        return dicts
