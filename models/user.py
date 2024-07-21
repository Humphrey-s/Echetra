#!/usr/bin/python3
"""User Model"""
from models.base_model import BaseModel


class User(BaseModel):
    username = ""
    first_name = ""
    last_name = ""
    university = ""
    interests = []
    email = ""
    field = ""
    mobile_number = ""
    country = ""
    location = ""
    projects = {}

    def __init__(self, *args, **kwargs):
        if kwargs is None:
            super().__init__(self, *args, **kwargs)
        else:

            if "id" not in kwargs.keys():
                super().__init__(self, *args, **kwargs)
                if "username" in kwargs.keys():
                    self.username = kwargs["username"]
                if "first_name" in kwargs.keys():
                    self.first_name = kwargs["first_name"]
                if "last_name" in kwargs.keys():
                    self.last_name = kwargs["last_name"]
                if "university" in kwargs.keys():
                    self.university = kwargs["university"]
                if "email" in kwargs.keys():
                    self.email = kwargs["email"]
                if "field" in kwargs.keys():
                    self.field = kwargs["field"]
                if "mobile_number" in kwargs.keys():
                    self.mobile_number = kwargs["mobile_number"]
                if "country" in kwargs.keys():
                    self.country = kwargs["country"]
                if "location" in kwargs.keys():
                    self.location = kwargs["location"]
                if "password" in kwargs.keys():
                    import bcrypt
                    salt = bcrypt.gensalt()
                    psswd = kwargs["password"]
                    hashed = bcrypt.hashpw(psswd.encode("utf-8"), salt)
                    self.password = hashed.decode("utf-8")
            else:
                for key, value in kwargs.items():
                    if key == "interests":
                        lst = self.interests
                        if isinstance(value, list):
                            for i in value:
                                if i not in lst:
                                    lst.append(i)
                        else:
                            lst.append(value)
                        value = lst
                        
                    setattr(self, key, value)
