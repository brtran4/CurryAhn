import flask
import requests
import arrow
import curryahn

@curryahn.app.route('/')
def show_index():
    return flask.render_template("index.html")