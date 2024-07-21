#!/usr/bin/python3
"""users api"""
from models import storage
from api.v1.pages import app_pages
from models.user import User
from models.projects import Project
from flask import jsonify, request, make_response


@app_pages.route("/users", methods=["GET"], strict_slashes=False)
def get_users():
    """get users json"""
    all_users = storage.all(User).values()
    lst = [user.to_dict() for user in all_users]

    return jsonify(lst)


@app_pages.route('/users/<user_id>', methods=["GET"], strict_slashes=False)
def get_user(user_id):
    """Get specific user"""
    obj = storage.get2(User, user_id)
    if obj is None:
        return 1
    else:
        return obj.to_dict()


@app_pages.route("/users/projects/<user_id>", methods=["GET"], strict_slashes=False)
def userprojects(user_id):
    """get projects for a certain user"""
    obj = storage.get2(User, user_id)

    if obj is None:
        return make_response(jsonify({"error": "user not found"}), 404)

    projects = storage.all(Project).values()
    lst = [p.to_dict() for p in projects if p.user_id == obj.id]

    return make_response(jsonify(lst), 200)
