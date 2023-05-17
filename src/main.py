import database, linkgen, config

db = database.load(config.database_file)

print(database.search_link(db, "oneb"))

# database.append(db, linkgen.generate_random_symbols(8), "ww.com")

database.write(config.database_file, db)
