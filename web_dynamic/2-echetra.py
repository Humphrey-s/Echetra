#!/usr/bin/python3
"""echetra main app"""
from flask import Flask, render_template, redirect, url_for
from flask import jsonify, make_response, request
from flask_session import Session
from flask_cors import CORS
from models import storage
from models.projects import Project
from web_dynamic.pages import app_pages
from web_dynamic.pages import session
from models.user import User
from uuid import uuid4

app = Flask(__name__)
app.register_blueprint(app_pages)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app)
app.config['SECRET_KEY'] = uuid4().hex
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.errorhandler(404)
def not_found(error):
    """handle 404 errors"""
    return make_response(jsonify({"error": "not found"}), 404)


@app.route('/Echetra/<username>/', methods=["POST", "GET"], strict_slashes=False)
def echetra(username):
    """ Echetra is Alive !"""
    all_users = storage.all(User)

    if session["id"] is None:
        return redirect(url_for("app_pages.plogin"))

    all_projects = storage.all(Project).values();
    user_projects = [p for p in all_projects if p.user_id == session["id"]];        
    session["projects"] = user_projects
    
    for user in all_users.values():
        if user.username == username:
            return render_template("2-echetra.html",
                user_id=session["id"],
                username=session["username"],
                projects=user_projects)


@app.route("/predashboard", methods=["GET"], strict_slashes=False)
def predashboard():
    """project session"""
    return redirect(f"/Echetra/{session['username']}")


@app.route("/Echetra/<username>/current", strict_slashes=False)
def echetra_project(username):
    """Echetra home"""
    all_users = storage.all(User).values()

    if session["username"] != username:
        return redirect(url_for("app_pages.login"));

    return render_template("main_project.html",
        username = session["username"],
        user_id = session["id"],
        projects = session["projects"]);


@app.route("/Echetra/<username>/home", methods=["GET", "POST"], strict_slashes=False)
def echetra_home(username):
    """Echetra home"""
    all_users = storage.all(User).values()

    if session["username"] != username:
        return redirect(url_for("app_pages.login"));

    return render_template("home.html",
        username = session["username"],
        user_id = session["id"],
        projects = session["projects"]);

@app.route("/Echetra/<username>/community", strict_slashes=False)
def echetra_community(username):
    """Echetra home"""
    all_users = storage.all(User).values()

    if session["username"] != username:
        return redirect(url_for("app_pages.login"));

    return render_template("community.html",
        username = session["username"],
        user_id = session["id"],
        projects = session["projects"]);

if __name__ == "__main__":
    """starts app application"""
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)
