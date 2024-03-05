#!/usr/bin/python3
"""
Defines the BaseModel class.
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Represents the BaseModel of project
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel instance.
        """
        if kwargs:
            """
            Initialize instance attributes from kwargs
            """
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """
        Update the arrtibute update_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        obj_di = self.__dict__.copy()
        obj_di['__class__'] = self.__class__.__name__
        obj_di['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        obj_di['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return obj_di

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        stname = self.__class__.__name__
        return "[{}] ({}) {}".format(stname, self.id, self.__dict__)
