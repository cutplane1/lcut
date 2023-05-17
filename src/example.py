import database, linkgen, config

# get json file
db = database.load(config.database_file)

# search link in db
print(database.search_link(db, "oneb"))

# add link
database.append(db, linkgen.generate_random_symbols(8), "ww.com")

# save link
database.write(config.database_file, db)
