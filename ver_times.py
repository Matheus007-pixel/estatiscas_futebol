import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT id, nome, escudo FROM times")
times = cursor.fetchall()

for t in times:
    print(t)

conn.close()
