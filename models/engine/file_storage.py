#!/usr/bin/python3
"""file storage engine"""
import json
import models
import os


class FileStorage():

    def __init__(self):
        self.__file = "file.json"
        self.__objects = {}

    def new(self, obj):
        """adds new object to self.__objects"""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj

    def all(self, cls=None):
        """retrieve stored objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.message import Message
        from models.projects import Project
        from models.task import Task
        from models.post import Post
        from models.message_session import Msession
        classes = {"BaseModel": BaseModel, "Post": Post, "User": User, "Message": Message, "Project": Project, "Msession": Msession}
        new_dct = {}

        if cls is not None:
            for key, value in self.__objects.items():
                if cls is value.__class__:
                    new_dct[key] = value
            return new_dct
        else:
            return self.__objects

    def save(self):
        """save object to file"""
        new_dict = {}
        for key, obj in self.__objects.items():
            new_dict[key] = obj.to_dict()

        with open(self.__file, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """stores objects in self.__objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.message import Message
        from models.projects import Project
        from models.task import Task
        from models.post import Post
        from models.message_session import Msession

        classes = {"BaseModel": BaseModel, "Post": Post, "User": User, "Msession": Msession,"Message": Message, "Project": Project, "Task": Task}
        if os.path.exists(self.__file):
            with open(self.__file, "r") as f:
                lst = json.load(f)
            for key, value in lst.items():
                d = value.copy()
                d.pop("__class__")
                self.__objects[key] = classes[value["__class__"]](**d)
                
        else:
            pass
    def delete(self, obj):
        """deletes an object"""
        objs = self.__objects.copy()
    
        for key, ob in objs.items():
            key1 = ob.__class__.__name__ + "." + str(ob.id)
            #print(f"{key}: {key1}")
            if ob.id == obj.id:
                del self.__objects[key]
                self.save()

    def close():
        """saves pending changes"""
        pass

    def get(self, object_id):
        """returns object with same id"""
        all_objects = self.all()

        for obj in all_objects.values():
            if obj.id == object_id:
                return obj
        else:
            return None

    def get2(self, cls, id):
         """returns object with same id"""
         from models.base_model import BaseModel
         from models.user import User
         from models.message import Message
         from models.projects import Project
         from models.message_session import Msession
         from models.task import Task
         from models.post import Post

         classes = {"BaseModel": BaseModel, "Post": Post, "Msession": Msession,"User": User, "Message": Message, "Project": Project, "Task": Task}

         if cls not in classes.values():
             return None

         for obj in self.all(cls).values():
             if obj.id == id:
                 return obj

    def get_messages(self, s_id, r_id):
        """get messages for a user"""
        from models.message import Message
        from models.user import User

        messages = self.all(Message).values()
        ids = [s_id, r_id]
        s_message = []

        for m in messages:
            user = self.get2(User, m.sender_id)
            m.sender_name = user.username
            if m.sender_id and m.recipient_id in ids:
                s_message.append(m)

        return s_message 
