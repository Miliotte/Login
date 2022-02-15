import sqlite3
from venv import create

conm = sqlite3.connect('Users.db')

cursor = conm.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    
);
""")