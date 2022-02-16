import sqlite3

conm = sqlite3.connect('Users.db')

cursor = conm.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    user TEXT NOT NULL,
    password TEXT NOT NULL
);
""")

print("Connected to Database")