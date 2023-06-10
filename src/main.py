import database, linkgen, config, decryptor

from flask import Flask, render_template, redirect, request

app = Flask(__name__)
db = database.load(config.DATABASE_FILE)

@app.route("/")
def main_page():
    return render_template('index.html')

@app.route("/<string:key>")
def redirect_page(key):
    return redirect("https://" + database.search_link(db, key))

@app.route("/s", methods=['POST'])
def save_page():
    sym = linkgen.generate_random_symbols(8)

    database.append(db, sym, request.form['link'])
    database.write(config.DATABASE_FILE, db)

    return config.URL + "/" + sym
