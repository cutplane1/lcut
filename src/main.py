from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('index.html')

@app.route("/s", methods=['POST'])
def save_page():
    return request.form['link']