# Создали базу данных
import sqlite3


db = sqlite3.connect('test_db.sqlite')
cursor = db.cursor()

cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    email TEXT NOT NULL UNIQUE
    )
''')





db.close()

