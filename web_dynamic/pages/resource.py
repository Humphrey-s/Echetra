#!/usr/bin/python3
from flask import Flask
from web_dynamic.pages import app_pages, session
from flask import make_response, jsonify, request
from werkzeug.utils import secure_filename
from models.post import Post
from models.user import User
from models.projects import Project
from models.message import Message
from models import storage
from models.message_session import Msession


month_dict = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "May",
    "06": "Jun",
    "07": "Jul",
    "08": "Aug",
    "09": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Decr"
}

@app_pages.route("/echetra/resource/post", methods=["POST"], strict_slashes=False)
def save_post_resource():
	"""save post resource"""
	import os
	folder = "web_dynamic/static/images/private/"
	filename = f"{session['id']}-"

	img = request.files["filename"]
	dc_t = {}

	if img:
		sfn = secure_filename(img.filename)
		sfn = f"{filename}{sfn}"
		img.save(os.path.join(folder, sfn))
		dc_t["media"] = os.path.join("../../../static/images/private/", sfn)
	
	dc_t["text"] = request.form.get("text")
	dc_t["user_id"] = session["id"]
	user = storage.get2(User, session["id"])
	dc_t["user"] = user.username

	instance = Post(**dc_t)
	instance.save()

	return jsonify(instance.to_dict())

@app_pages.route("/echetra/resource/message", methods=["POST"], strict_slashes=False)
def save_message():
	"""Save message"""
	dc_t = {}
	dc_t = {
		"Msession_id": request.form.get("Msession_id"),
		"message": request.form.get("text"),
		"sender_id": request.form.get("sender_id"),
		"recipient_id": request.form.get("recipient_id"),
		"sender_name": storage.get2(User, request.form.get("sender_id")).username,
		"recipient_name": storage.get2(User, request.form.get("recipient_id")).username
		}

	msession = storage.get2(Msession, dc_t["Msession_id"])
	
	instance = Message(**dc_t)

	if msession is not None:
		msession.messages.append(instance.to_dict())
		msession.save()

	return jsonify(instance.to_dict())


@app_pages.route("/echetra/resource/post_session", methods=["POST"])
def save_tsession():
	"""saves to session"""
	file = request.form.get("")
	print(file)
	return jsonify("Ok")

@app_pages.route("/echetra/r/u/<user_id>/posts", methods=["GET"], strict_slashes=False)
def get_posts(user_id):
	"""get posts of a user id"""
	from datetime import date, datetime
	dformat = ""

	user = storage.get2(User, user_id)

	if user is None:
		return "Ok"


	posts = storage.all(Post).values()
	user_posts = [p.to_dict() for p in posts if p.user_id == user.id]
	new_lst = []

	for up in user_posts:
		d_time = up["created_at"]
		d = d_time.split(" ")[0]
		dd = d.split("-")[2]
		d_month = month_dict[d_time.split("-")[1]]

		Tmonth = date.today().month
		Tyear = date.today().year
		Tdate = date.today().strftime("%Y-%m-%d")
		Ttime = datetime.utcnow().strftime("%H:%M:%S")

		if Tdate != d:
			up["created_at"] = f"{dd} {d_month}"
		else:
			up["created_at"] = "Today"
		
		new_lst.append(up)


	return jsonify(new_lst)


@app_pages.route("/echetra/r/u/<user_id>/p", methods=["GET"], strict_slashes=False)
def userprojects(user_id):
    """get projects for a certain user"""
    obj = storage.get2(User, user_id)
    from datetime import date, datetime

    if obj is None:
        return make_response(jsonify({"error": "user not found"}), 404)

    projects = storage.all(Project).values()
    lst = [p.to_dict() for p in projects if p.user_id == obj.id]
    new_lst = []

    for up in lst:
    	d_time = up["created_at"]
    	d = d_time.split(" ")[0]
    	dd = d.split("-")[2]
    	d_month = month_dict[d_time.split("-")[1]]

    	Tmonth = date.today().month
    	Tyear = date.today().year
    	Tdate = date.today().strftime("%Y-%m-%d")
    	Ttime = datetime.utcnow().strftime("%H:%M:%S")

    	if Tdate != d:
    		up["created_at"] = f"{dd} {d_month}"
    	else:
    		up["created_at"] = "Today"

    	new_lst.append(up)


    return make_response(jsonify(new_lst), 200)