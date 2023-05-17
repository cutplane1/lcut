import json

def load(file_link):
    with open(file_link) as json_file:
        return json.load(json_file)


def write(file_link, db):
    with open(file_link, "w") as json_file:
        json.dump(db, json_file, sort_keys=True, indent=2)


def append(db, key, link):
    db[key] = link


def search_link(db, key):
    return db[key]