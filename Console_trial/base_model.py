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
        di = self.__dict.copy()
        di['created_at'] = self.created_at.isoformat()
        di['updated_at'] = self.updated_at.isoformat()
        return di

    def __str__(self):
        return ("[{:s}] ({:s}) {:s} {:s}".format(self.__class__.__name__, self.id, self.__dict__))
