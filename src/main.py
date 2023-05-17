import database, linkgen, config

from flask import Flask, render_template, request

app = Flask(__name__)
db = database.load(config.database_file)

@app.route("/")
def main_page():
    return render_template('index.html')

@app.route("/s", methods=['POST'])
def save_page():
    sym = linkgen.generate_random_symbols(8)

    database.append(db, sym, request.form['link'])
    database.write(config.database_file, db)

    return config.URL + "/" + sym