import flask
import requests
import arrow
import curryahn
import curryahn.model
from curryahn.model import get_db


@curryahn.app.route('/accounts/login/', methods=["GET"])
def login():
    if "username" in flask.session:
        return flask.redirect(flask.url_for("show_index"))
    return flask.render_template("login.html")

@curryahn.app.route('/accounts/', methods=["POST"])
def handle_accounts():
    data = get_db()
    if flask.request.form["operation"] == "login":
        login_helper(data)
    
    targeturl = flask.request.args.get("target")
    if targeturl is None:
        return flask.redirect(flask.url_for("show_index"))
    return flask.redirect(targeturl)

def login_helper(data):
    username = flask.request.form["username"]
    password = flask.request.form["password"]
    users = data.execute("SELECT * FROM STUDENTS")
    if username is None or password is None:
        return flask.abort(400)
    for user in users:
        if user["username"] == username and user["password"] == password:
            flask.session["username"] = username
            flask.session["password"] = password

@curryahn.app.route('/accounts/logout/', methods=['POST'])
def logout():
    flask.session.pop("username", None)
    return flask.redirect(flask.url_for("login"))