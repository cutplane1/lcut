import database

db = database.load()

database.search_link(db, "oneb")

# database.append(db, "ttb", "ww.com")

database.write(db)