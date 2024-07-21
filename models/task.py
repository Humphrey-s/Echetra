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
            if "id" in kwargs.keys():
                for key, value in kwargs.items():
                    setattr(self, key, value)
            else:
                super().__init__(self, *args, **kwargs)
                for key, value in kwargs.items():
                    setattr(self, key, value)
        else:
            super().__init__(self, *args, **kwargs)
