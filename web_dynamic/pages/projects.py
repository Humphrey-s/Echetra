#!/usr/bin/python3
from flask import Flask
from web_dynamic.pages import app_pages, session
from flask import redirect, url_for, request, flash, render_template
from models import storage
from models.user import User
from models.projects import Project
from models.task import Task

project_name = {}


@app_pages.route("/dashboard/create9project", methods=["POST", "GET", "DELETE"], strict_slashes=False)
def create_project():
    """create new project"""
    dct = {}
    name = request.form.get("name");
    p_id = request.form.get("id");
    dct["name"] = name
    dct["id"] = p_id
    dct["user_id"] = session.get("id")

    return redirect(url_for("app_pages.project", id=p_id, name=name, user_id=dct["user_id"]))

@app_pages.route("/project", methods=["POST", "GET", "DELETE"], strict_slashes=False)
def project():
    """project session"""
    pid = request.args.get("id")
    user_id = request.args.get("user_id")
    project_name = request.args.get("name")

    all_task = storage.all(Task).values()

    ptasks = [task.to_dict() for task in all_task if task.project_id == pid]

    return render_template("project.html", id=pid, project=project_name, tasks=ptasks)
