#!/usr/bin/python3
"""
module base model
"""
from uuid import uuid4
from datetime import datetime 


class BaseModel:
    """
    a class defining all common attributes
    and or methods for all other classes
    """
    def __init__(self):
        """
        initialize the attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        update the current update_at
        """
        self.updated_at = datetime.now

    def to_dict(self):
        """
        returns a dictionary containing all keys of __dict__
        """
        

    def __str__(self):
        return ("[{:s}] ({:s}) {:s} {:s}".format(self.__class__.__name__, self.id, self.__dict__))
