#!/usr/bin/python3
from flask import Flask, session, jsonify, make_response, request, abort
from api.v1.pages import app_pages
from datetime import datetime
from models import storage
from models.task import Task


@app_pages.route("/tasks/<task_id>", methods=["GET"], strict_slashes=False)
@app_pages.route("/tasks", methods=["GET"], strict_slashes=False)
def get_tasks(task_id=None):
    """get tasks for projects"""
    if task_id is None:
        tasks = [task.to_dict() for task in storage.all(Task).values()]
        return jsonify(tasks)

    task_obj = storage.get(task_id)
    if task_obj is None:
        abort(404, "not found")

    return jsonify(task_obj.to_dict())

@app_pages.route("/createTask", methods=["POST"], strict_slashes=False)
def create_task():
    """create task"""
    if request.get_json() is None:
        abort(404, "No data")

    dct = {}

    data = request.get_json()
    dct["project_id"] = data["pid"]
    dct["name"] = data["taskName"]

    if "startDate" in data.keys():
        dct["startDate"] = data["startDate"]
    else:
        dct["start_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dct["end_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    instance = Task(**dct)
    instance.save()
    storage.reload()
    return jsonify(instance.to_dict())

@app_pages.route("/updateTask/<task_id>", methods=["PUT"], strict_slashes=False)
def  update_task(task_id):
    """update task"""
    if request.get_json() is None:
        abort(404, "No data")

    dct = {}
    data = request.get_json()
    ignore = ["created_at", "updated_at", "id", "project_id", "user_id"]

    obj = storage.get(task_id)
    if obj is None:
        abort(400, "bad request")

    for key, value in data.items():
        if key not in ignore:
            setattr(obj, key, value)
    storage.save()
    storage.reload()
    return make_response(jsonify(obj.to_dict())), 200
