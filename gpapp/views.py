from flask import render_template, jsonify, request

from . import app
from gpapp.grandpy import GrandPy


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/grandpy", methods=["POST"])
def place_info():
    grandpy = GrandPy()
    user_text = request.form["userText"]
    response = grandpy.grandpy_answer(user_text)
    return jsonify(response)
