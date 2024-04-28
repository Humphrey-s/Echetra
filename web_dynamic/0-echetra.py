#!/usr/bin/python3
"""echetra main app"""
from flask import Flask, render_template, redirect, url_for
from flask import jsonify, make_response, request
from flask_cors import CORS
from models import storage
from models.user import User
from web_dynamic.pages import app_pages
from uuid import uuid4

app = Flask(__name__)
app.register_blueprint(app_pages)

app.config['SECRET_KEY'] = uuid4().hex

@app.errorhandler(404)
def not_found(error):
    """handle 404 errors"""
    return make_response(jsonify({"error": "not found"}), 404)

@app.route('/echetra', methods=["POST", "GET"], strict_slashes=False)
def echetra():
    """ Echetra is Alive !"""
    all_users = storage.all(User).values()
    user_lst = []

    for user in all_users:
        user_lst.append(user.username)

    return render_template(
            "0-echetra.html",
            users=user_lst
            )

@app.route("/dashboard")
def main_dashboard():
    """main dashboard"""
    return render_template("alechtra.html")

if __name__ == "__main__":
    """starts app application"""
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)
