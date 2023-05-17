import database, linkgen

db = database.load()

# database.search_link(db, "oneb")

database.append(db, linkgen.generate_random_symbols(8), "ww.com")

database.write(db)
