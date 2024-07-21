#!/usr/bin/python3
"""login authentication and redirection"""
from web_dynamic.pages import app_pages
from flask import redirect, url_for, request, flash, render_template, session
from models import storage
from models.user import User
import bcrypt
from uuid import uuid4


@app_pages.route("/echetra/loginauth", methods=["POST"], strict_slashes=False)
def login_post():
    """login authentication"""
    username = request.form.get("username")
    password = request.form.get("passwd")

    all_users = storage.all(User).values()

    usernames_dct = {user.username: user for user in all_users}

    if username in usernames_dct.keys():
        user = usernames_dct[username]
        username1 = user.username;
        user_id = user.id
        passwd = user.password.encode("utf-8")

        r = bcrypt.checkpw(password.encode("utf-8"), passwd)
        if r is True:
            session["username"] = username1
            session["id"] = user_id
            flash("signed in successfully")
            return redirect(url_for("predashboard"))
        else:
            flash(f"Invalid credentrials: {r}")
            return redirect(url_for("app_pages.plogin"))
    else:
        flash("Invalid credentrials")
        return redirect(url_for("app_pages.plogin"))


@app_pages.route("/echetra/login", methods=["POST", "GET"], strict_slashes=False)
def plogin():
    """return login page"""
    return render_template("login.html",
        cache_id = uuid4())


@app_pages.route("/echetra/signUp", methods=["POST", "GET"], strict_slashes=False)
def psignup():
    """sign up"""
    return render_template("signUp.html", cache_id = uuid4())


@app_pages.route("/echetra/signlauth", methods=["POST", "GET"], strict_slashes=False)
def signUp():
    """handles sign up data"""
    username = request.form.get("username")
    passwd1 = request.form.get("passwd1")
    passwd2 = request.form.get("passwd2")

    if username is None:
        flash("field empty")
        return redirect(url_for("app_pages.psignup"))
    else:
        all_users = storage.all(User).values()
        lst_usernames = [user.username for user in all_users]

        if username in lst_usernames:
            flash("Username already Exists")
            return redirect(url_for("app_pages.psignup"))
        else:
            if passwd2 is None:
                flash("weak password")
                return redirect(url_for("app_pages.psignup"))
            else:
                dct = {"username": username, "password": passwd2}
                instance = User(**dct)
                instance.save()
                storage.save()
                storage.reload()

                return redirect(url_for("app_pages.plogin"))
