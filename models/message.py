#!/usr/bin/python3
"""messages"""
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.message_session import Msession


class Message(BaseModel):

    Msession_id = ""
    sender_id = ""
    sender = ""
    recipient_id = ""
    recipient = ""
    message = ""

    def __init__(self, *args, **kwargs):
        """initialize message instance"""
        if kwargs is not None:
            if "id" in kwargs.keys():
                for key, value in kwargs.items():
                    setattr(self, key, value)
            else:
                super().__init__(self, *args, **kwargs)
                for key, value in kwargs.items():
                    setattr(self, key, value)
        else:
            super().__init__(self, *args, **kwargs)
