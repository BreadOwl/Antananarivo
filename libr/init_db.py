import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, author, description) VALUES (?, ?, ?)",
            ('First Book', 'Wise Man', 'It is good book')
            )

cur.execute("INSERT INTO posts (title, author, description) VALUES (?, ?, ?)",
            ('Second Book', 'Another Wise Man', 'It is good book')
            )

connection.commit()
connection.close()
