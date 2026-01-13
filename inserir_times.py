import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

times = [
    ("Flamengo", 5, 10),
    ("Palmeiras", 5, 8),
    ("Corinthians", 5, 6)
]

cursor.executemany(
    "INSERT INTO times (nome, jogos, gols) VALUES (?, ?, ?)",
    times
)

conn.commit()
conn.close()

print("Times inseridos com sucesso!")
