#!/usr/bin/python3
from flask import Flask
from web_dynamic.pages import app_pages, session
from flask import redirect, url_for, request, flash, render_template, make_response
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

@app_pages.route("/Echetra/<username>/<pname>", strict_slashes=False)
def user_project(username, pname):
    """user navigation"""
    all_users = storage.all(User).values()

    for user in all_users:
        if user.username == username:
            projects = storage.all(Project).values()
            for p in projects:
                if p.name == pname:
                    return redirect(url_for("app_pages.project", id=p.id, name=p.name, user_id=user.id))
            else:
                return make_response({"error": "project not found"}, 400)

    return make_response({"error": "user not found"}, 400)
