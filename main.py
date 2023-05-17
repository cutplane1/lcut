import json

def load():
    with open("db.json") as json_file:
        return json.load(json_file)


def write():
    with open("db.json", "w") as json_file:
        json.dump(db, json_file, sort_keys=True, indent=2)


db = load()

# db.append({"file_path": "C:\\folder\\pic.png", "tags": ["cat", "kot"]})

# write()
