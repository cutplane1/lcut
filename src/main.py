from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return "<p>Hello, World!</p>"