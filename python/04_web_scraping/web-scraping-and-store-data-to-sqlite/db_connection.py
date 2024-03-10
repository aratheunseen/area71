import sqlite3

# connection and cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# read/fetch data
cursor.execute('SELECT email FROM users WHERE id=4')
rows = cursor.fetchall()
print(rows)

# insert data
new_data = [(3,'Abdul', 'abd@ul.com', '122445'),
            (4,'Jobdul', 'job@dul.net', '54778544')]

cursor.executemany("INSERT INTO users VALUES(?,?,?,?)", new_data)
connection.commit()