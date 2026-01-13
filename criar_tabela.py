import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS times (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    jogos INTEGER,
    gols INTEGER
)
""")

conn.commit()
conn.close()

print("Tabela criada com sucesso!")
