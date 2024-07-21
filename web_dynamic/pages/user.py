#!/usr/bin/python3
from flask import Flask
from web_dynamic.pages import app_pages, session
from flask import redirect, url_for, jsonify, request, flash, render_template, make_response
from models import storage
from models.user import User
from models.projects import Project
from models.task import Task


@app_pages.route("/Echetra/user/<user_id>", methods=["PUT"], strict_slashes=False)
def update_user(user_id):
	"""update user"""
	user = storage.get2(User, user_id)
	dc_t = request.form

	new_dict = user.to_dict()

	for key, value in dc_t.items():
		if value != "" and key != "user_id":
			new_dict[key] = value

	instance = User(**new_dict)
	instance.save()

	return jsonify(instance.to_dict())