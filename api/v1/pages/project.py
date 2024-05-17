#!/usr/bin/python3
from models import storage
from models.projects import Project
from models.task import Task
from flask import Flask, request, jsonify, abort, make_response
from api.v1.pages import app_pages
import json


@app_pages.route("/projects", strict_slashes=False)
def projects():
    """return json for projects"""
    all_projects = storage.all(Project)

    dct = [p.to_dict() for p in all_projects.values()]
    return dct

@app_pages.route("/projects/<p_id>", methods=["GET"], strict_slashes=False)
def get_project(p_id=None):
    """returns a project"""
    all_projects = storage.all(Project)
    d = [p.to_dict() for p in all_projects.values()]

    if p_id is None:
        return d

    for project in all_projects.values():
        if project.id == p_id:
            return project.to_dict()

    return {"error": "not found"}

@app_pages.route("/projects/tasks/<p_id>", methods=["GET"], strict_slashes=False)
def get_ptasks(p_id=None):
    """get tasks for a given project"""
    obj = storage.get(p_id)

    if obj is None:
        abort(404, "{error: project not found}")

    all_tasks = storage.all(Task).values()

    lst = [task.to_dict() for task in all_tasks if task.project_id == p_id]

    return jsonify(lst)

@app_pages.route("/create9project", methods=["POST"], strict_slashes=False)
def add_project():
    """create new project"""
    
    if request.get_json() is None:
        abort(400, "Not json")

    data = request.get_json()

    instance = Project(**data)
    instance.save()

    return jsonify(instance.to_dict())


@app_pages.route("/projects/<p_id>", methods=["PUT"], strict_slashes=False)
def update_project(p_id=None):
    """returns a project"""
    all_projects = storage.all(Project)
    d = [p.to_dict() for p in all_projects.values()]

    if p_id is None:
        return jsonify(d)

    for obj in all_projects.values():
        if obj.id == p_id:
            content = request.data.decode("utf-8")
            array = content.split("=")
            dct = {}
            if array[0] == "task":
                obj.tasks.append(array[1])
                obj.save()
                return obj.to_dict()

    return "{}"
