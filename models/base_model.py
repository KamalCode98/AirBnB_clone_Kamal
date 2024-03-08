#!/usr/bin/python3
"""
Module for BaseModel
"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args,**kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        for key, value in kwargs.items():
            if key != "__class__":
                setattr(self, key, value)
            if key == "created_at" or key == "updated_at":
                setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.upload_at = datetime.now
        
    def to_dict(self):
        dictionary = slef.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary