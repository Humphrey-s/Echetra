#!/usr/bin/python3
from models.base_model import BaseModel


class Task(BaseModel):
    """Task project"""

    name = ""
    project_id = ""
    subtasks = {}
    completed = ""
    startDate = ""
    endDate = ""

    def __init__(self, *args, **kwargs):
        """initialization"""
        if kwargs is not None:
            super().__init__(*args, **kwargs)

            if "name" in kwargs.keys():
                self.name = kwargs["name"]
            if "project_id" in kwargs.keys():
                self.project_id = kwargs["project_id"]
            if "startDate" in kwargs.keys():
                self.startDate = kwargs["startDate"]
            if "endDate" in kwargs.keys():
                self.endDate = kwargs["endDate"]
            if "completed" in kwargs.keys():
                self.completed = kwargs["completed"]
