#!/usr/bin/python3
"""messages"""
from models.base_model import BaseModel
from models import storage
from models.user import User


class Message(BaseModel):

    sender_id = ""
    sender = ""
    recipient_id = ""
    message = ""

    def __init__(self, *args, **kwargs):

        if "status" in kwargs.keys():
            super().__init__(**kwargs)
        else:
            super().__init__()
            users = storage.all(User)
            if kwargs is not None:
                if "username" in kwargs.keys():
                    username = kwargs["username"]
                    for user in users.values():
                        if user.username == username:
                            sender = user
                            self.sender = username
                            self.sender_id = user.id
                if "recipient" in kwargs.keys():
                    for user in users.values():
                        if user.username == kwargs['recipient']:
                            recipient = user
                            self.recipient = kwargs['recipient']
                            self.recipient_id = user.id

                if "message" in kwargs.keys():
                    self.message = kwargs["message"]


            if self.sender_id is None or "":
                self.status = "not sent"
                self.error = "** sender not found **"
            else:
                if self.recipient_id is None or "":
                    self.status = "not sent"
                    self.error = "** recipient not found**"
                else:
                    if self.message is None or "":
                        self.status = "not sent"
                        self.error = "** message not found **"
                    else:
                        lst = []
                        self.status = "sent"
                        lst.append(self.to_dict())
                        outbox = sender.outbox
                        if recipient.username in outbox.keys():
                            outbox[recipient.username].append(self.to_dict())
                            sender.outbox = outbox
                        else:
                            outbox[recipient.username] = lst
                            sender.outbox = outbox

                        inbox = recipient.inbox
                        if sender.username in inbox.keys():
                            inbox[sender.username].append(self.to_dict())
                            recipient.inbox = inbox
                        else:
                            inbox[sender.username] = lst
                            recipient.inbox = inbox

            storage.delete(recipient)
            storage.delete(sender)
            storage.save()
            storage.new(recipient)
            storage.new(sender)
            storage.save()
