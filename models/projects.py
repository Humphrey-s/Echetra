#!/usr/bin/python3
"""projects"""
from models.base_model import BaseModel


class Project(BaseModel):

    name = ""
    category = ""
    description = ""
    features = ""
    presentation = []
    url = []
    tasks = []
    pictures = []
    user_id = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self)
        if kwargs is not None:
            if "name" in kwargs.keys():
                self.name = kwargs["name"]
            if "category" in kwargs.keys():
                self.category = kwargs["category"]
            if "description" in kwargs.keys():
                self.description = kwargs["description"]
            if "startDate" in kwargs.keys():
                self.startDate = kwargs["startDate"]
            if "endDate" in kwargs.keys():
                self.endDate = kwargs["endDate"]
            if "presentation" in kwargs.keys():
                self.presentation.append(kwargs["presentation"])
            if "url" in kwargs.keys():
                self.url.append(kwargs["url"])
            if "tasks" in kwargs.keys():
                self.pictures.append(kwargs["tasks"])
            if "user_id" in kwargs.keys():
                self.user_id = kwargs["user_id"]
