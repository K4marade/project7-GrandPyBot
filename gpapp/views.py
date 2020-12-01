from flask import render_template, jsonify, request

from . import app
from .utils.parser import Parser as par


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/question', methods=["POST"])
def question():
    user_text = request.form["userText"]
    response = par(user_text).process()
    return jsonify(response)
