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
from models.post import Post
from models import storage
from models.message import Message
from models.message_session import Msession
from uuid import uuid4
import json
from flask_socketio import join_room, leave_room, send, SocketIO
import requests as r
import smtplib, ssl
from uuid import uuid4


app = Flask(__name__)
app.register_blueprint(app_pages)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app)
app.config['SECRET_KEY'] = uuid4().hex
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

socketio = SocketIO(app)
public_room = "community"


@app.errorhandler(404)
def not_found(error):
    """handle 404 errors"""
    return make_response(jsonify({"error": "not found"}), 404)

@app.route("/echetra", methods=["GET"], strict_slashes=False)
def main_echetra():
    return render_template("echetra_main.html")


@app.route("/predashboard", methods=["GET"], strict_slashes=False)
def predashboard():
    """project session"""
    return redirect(f"/Echetra/{session['username']}")


@app.route("/echetra/projects", strict_slashes=False)
def echetra_project():
    """Echetra home"""
    all_users = storage.all(User).values()
    username = storage.get2(User, session["user_id"]).username

    if session["username"] != username:
        return redirect(url_for("app_pages.plogin"));

    return render_template("main_project.html",
        username = session["username"],
        user_id = session["user_id"],
        projects = session["projects"],
        cache_id = uuid4());


@app.route("/echetra/home", methods=["GET", "POST"], strict_slashes=False)
def echetra_home():
    """Echetra home"""
    all_users = storage.all(User).values()
    username = storage.get2(User, session["user_id"]).username

    return render_template("home.html",
        username = username,
        user = storage.get2(User, session["user_id"]),
        user_id = session["user_id"],
        projects = session["projects"],
        cache_id = uuid4());


@app.route("/echetra/community/home", strict_slashes=False)
@app.route("/echetra/community", strict_slashes=False)
def echetra_community():
    """Echetra home"""
    storage.reload()
    all_users = storage.all(User).values()
    all_posts = storage.all(Post).values()
    user = storage.get2(User, session["user_id"])


    if session["username"] != user.username:
        return redirect(url_for("app_pages.plogin"));

    #hackathons = r.get("http://localhost:5001/hackathons/upcoming/filtered")
    #hackathons = hackathons.json()

    return render_template("community.html",
        username = session["username"],
        user_id = session["user_id"],
        user = user,
        projects = session["projects"],
        posts = all_posts,
        cache_id = uuid4()
        )


@app.route("/echetra/chess", strict_slashes=False)
def echetra_chess():
    """chess application"""
    storage.reload()
    all_users = storage.all(User).values()
    all_posts = storage.all(Post).values()
    user = storage.get2(User, session["user_id"])

    return render_template("chess.html",
        username = session["username"],
        user_id = session["user_id"],
        user = user,
        projects = session["projects"],
        posts = all_posts,
        cache_id = uuid4()
        );


@app.route("/echetra/community/members")
def echetra_community_members():
    """Echetra community members"""
    storage.reload()
    all_users = storage.all(User).values()
    user = storage.get2(User, session["user_id"])

    if session["username"] != user.username:
        return redirect(url_for("app_pages.plogin"));

    return render_template("community_members.html",
        username = session["username"],
        user_id = session["user_id"],
        no_users = len(all_users),
        cache_id = uuid4()
        )   


@app.route("/echetra/community/message/<user_id>")
def echetra_comunity_mmessage(user_id):
    """url for messaging a user"""
    storage.reload()
    all_users = storage.all(User).values()
    all_msession = storage.all(Msession).values()

    if user_id == session["user_id"]:
        return redirect(url_for(echetra_community_members))

    for s in all_msession:
        if user_id in s.users:
            if session["id"] in s.users:
                return redirect(f"/echetra/message/{s.id}")
    else:
        dct = {}
        dct["users"] = [user_id, session["user_id"]]
        s = Msession(**dct)
        s.save()
        return redirect(f"/echetra/message/{s.id}")


@app.route("/echetra/message/<Msession_id>", strict_slashes=False)
def echetra_message(Msession_id):
    """url for messaging session btwn 2 users"""
    storage.reload()
    msession = storage.get2(Msession, Msession_id)

    for id in msession.users:
        if id == session["user_id"]:
            sender = storage.get2(User, id)
        else:
            recipient = storage.get2(User, id)
    else:
        return render_template("community_mmessages2.html",
            user = sender.to_dict(),
            recipient = recipient.to_dict(),
            messages = msession.messages,
            msession = msession
        ) 




@app.route("/echetra/community/messages")
def echetra_messages():
    """url for message"""
    storage.reload()
    all_users = storage.all(User).values()
    user = storage.get2(User, session["user_id"])

    if session["username"] != user.username:
        return redirect(url_for("app_pages.plogin"));

    return render_template("message.html",
        username = session["username"],
        friends = all_users,
        cache_id = uuid4()
        ); 


def send_emailCode(receiver_email):
    """sends email code"""
    port = 465 

    code = str(uuid4())
    code = code[-4:]

    smtp_server = "smtp.gmail.com"
    sender_email = "echetrateam@gmail.com"
    password = "bdry zmnz gcrg plaz"


    message = f"""\
    Your sign-in code: {code}
    Please copy and paste the 6-digit code below into the number fields of your sign-in process. {code}
    """

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    return code


def get_user_projects(user_id):
    """get user projects"""
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


    return new_lst


@app.route("/echetra/signin/code", methods=["GET", "POST"], strict_slashes=False)
def echetra_scode():
    """echetra signin code"""
    email = request.form.get("email")
    code = send_emailCode(email)

    return render_template("sicode.html", code=code, email=email, cache_id=uuid4())


@app.route("/echetra/Oauth", methods=["POST"], strict_slashes=False)
def authorize():
    """authorize login"""
    email = request.form.get("email");
    storage.reload();
    users = storage.all(User).values();

    for u in users:
        if u.email == email:
            session["user_id"] = u.id
            session["projects"] = get_user_projects(u.id)
            session["username"] = u.username
            return redirect(url_for("echetra_home"))
    else:
        kwargs = {"email": email}
        instance = User(**kwargs)
        instance.save()
        session["uninitialized_user"] = instance.id;

        return redirect(url_for("onboarding1"))


@app.route("/echetra/signup/onboarding-step1")
def onboarding1():
    """onboarding-step1"""
    return render_template("onboarding.html")

@app.route("/echetra/signup/onboarding-step2", methods=["GET", "POST"])
def onboarding2():
    """onboarding step 2"""
    user_id = session["uninitialized_user"]
    user = storage.get2(User, user_id)

    user.name = request.form.get("name")
    user.username = request.form.get("name").split(" ")[0]
    user.save()
    print(user.to_dict())

    return render_template("onboarding2.html"); 

@app.route("/echetra/signup/onboarding-end")
def onboading_end():
    """onboading end"""
    user_id = session["uninitialized_user"]
    user = storage.get2(User, user_id)

    user.occupation = request.form.get("occupation")
    user.interests.append(request.form.get("interests"))
    user.schoolLevel = request.form.get("schoolLevel")

    session["user_id"] = user.id
    session["projects"] = get_user_projects(user.id)
    return redirect(url_for("echetra_home"))


@app.route("/echetra/")
@socketio.on('connect')
def connect(auth):
    """connect main"""
    join_room(public_room)


@socketio.on("post")
def post(data):
    """send posts to users"""
    socketio.emit('main_post', data);

@socketio.on("message")
def message(data):
    """send Message"""
    dc_t = {}
    user = storage.get2(User, data["sender_id"])
    dc_t["sender"] = user.to_dict()
    dc_t["message"] = data

    socketio.emit('main_message', dc_t)

if __name__ == "__main__":
    """starts app application"""
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
