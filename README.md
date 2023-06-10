# LCut (Link Cut)

Simple link shortener in python and flask.

## Start App

```
flask --app src/main run
```

## Config
DATABASE_FILE -> json file <br>
URL -> app web address

Example:
```
import os

DATABASE_FILE = os.path.join(os.getcwd(), "db.json")
URL = "127.0.0.1:5000"
```

## Using Modules

```
import database, linkgen, config

# get json file
db = database.load(config.DATABASE_FILE)

# search link in db
print(database.search_link(db, "Ax2Ui3"))

# add link
database.append(db, linkgen.generate_random_symbols(8), "example.com")

# save link
database.write(config.DATABASE_FILE, db)
```

## Template Form
stored in "templates/index.html"

Example:
```
<form action="/s" method="POST">
    <input name="link" type="text"><br> <!-- input name should be "link" -->
    <input type="submit" value="submit_button">
</form>
```
