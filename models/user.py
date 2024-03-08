#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user
    
    Arrtibutes
    * email : str
    * password : str
    * first_name : str
    * last_name : str
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""