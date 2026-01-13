import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
ALTER TABLE times
ADD COLUMN escudo TEXT
""")

conn.commit()
conn.close()

print("Coluna escudo adicionada!")
