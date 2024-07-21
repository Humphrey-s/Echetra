#!/usr/bin/python3
"""messages"""
from models.base_model import BaseModel
from models import storage
from models.user import User


class Msession(BaseModel):

    users = []
    messages = []

    def __init__(self, *args, **kwargs):
        """initialize message instance"""
        from models.message import Message
        if kwargs is not None:
            if "id" in kwargs.keys():
                for key, value in kwargs.items():
                    if key == "message":
                        self.messages.append(value)
                    else:
                        setattr(self, key, value)
            else:
                super().__init__(self, *args, **kwargs)
                for key, value in kwargs.items():
                    if key == "message":
                        self.messages.append(value)
                    else:
                        setattr(self, key, value)
        else:
            super().__init__(self, *args, **kwargs)