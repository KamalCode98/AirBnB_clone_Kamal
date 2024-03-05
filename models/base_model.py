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

    def __init__(self):
        """
        Initialize BaseModel instance.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Return string representation of BaseModel.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the arrtibute update_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary
        containing all keys and values of __dict__ of the instance.
        """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
