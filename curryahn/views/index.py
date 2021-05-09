import flask
import requests
import arrow
import curryahn

@curryahn.app.route('/')
def show_index():
    if "username" not in flask.session:
        return flask.redirect(flask.url_for("login"))
    return flask.render_template("index.html")