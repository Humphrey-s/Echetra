#!/usr/bin/python3
"""login authentication and redirection"""
from web_dynamic.pages import app_pages
from flask import redirect, url_for, request, flash
from models import storage
from models.user import User

@app_pages.route("/login", methods=["POST"], strict_slashes=False)
def login_post():
    """login authentication"""
    username = request.form.get("username")
    password = request.form.get("passwd")

    all_users = storage.all(User).values()

    print(all_users)

    usernames_lst = [user.username for user in all_users]
    if username in usernames_lst:
        return redirect(url_for("main_dashboard"))
    else:
        flash("username not found")
        return redirect(url_for("echetra"))
