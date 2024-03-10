import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()


cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()

print(rows)