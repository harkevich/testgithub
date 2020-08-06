# import sqlite3
#
#
# db = sqlite3.connect('test_db.sqlite')
# cursor = db.cursor()
#
# email = 'petrov2@gmail.com'

# cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")

# cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
# cursor.execute("SELECT * FROM users WHERE email = ? or name = ?", (email, "John Doe"))
# cursor.execute("SELECT * FROM users WHERE email = :email or name = :name", {"email": email,
# "name": "John Doe"})

# cursor.execute("SELECT * FROM users")
# res = cursor.fetchone()     # Выводит одну запись в виде кортежа
# res2 = cursor.fetchall()    # Выводит все записи в виде списка кортежей

# print(res)
# print(res2)
# for user in res2:
#     print(user[1], user[2])

# db.close()
# -----------------------------------------------------
# import sqlite3
# def dict_factory(cur, row):
#     d = {}
#     for idx, col in enumerate(cur.description):
#         d[col[0]] = row[idx]
#     return d
#
# db = sqlite3.connect('test_db.sqlite')
#
# db.row_factory = dict_factory
#
# cursor = db.cursor()
# email = 'petrov@gmail.com'
#
# cursor.execute("SELECT * FROM users")
#
# res = cursor.fetchall()
#
# print(res)
# for user in res:
#     print(user["name"], user["email"])
# db.close()

# -----------------------------------------------------
import sqlite3
def dict_factory(cur, row):
    d = {}
    for idx, col in enumerate(cur.description):
        d[col[0]] = row[idx]
    return d

db = sqlite3.connect('test_db.sqlite')

db.row_factory = dict_factory
cursor = db.cursor()

db.total_changes

cursor.execute('INSERT INTO users (name, email) VALUES ("User 4", "user4@gmail.com")')
cursor.execute('INSERT INTO users (name, email) VALUES ("User 5", "user5@gmail.com")')

db.commit()
print(db.total_changes)

db.close()