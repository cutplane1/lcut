import json

def load():
    with open("db.json") as json_file:
        return json.load(json_file)


def write(db):
    with open("db.json", "w") as json_file:
        json.dump(db, json_file, sort_keys=True, indent=2)


def append(db, key, link):
    db[key] = link


def search_link(db, key):
    return db[key]


db = load()

search_link(db, "oneb")

append(db, "ttb", "ww.com")

write(db)