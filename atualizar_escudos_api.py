import sqlite3

escudos = {
    "Flamengo": "https://media.api-sports.io/football/teams/127.png",
    "Palmeiras": "https://media.api-sports.io/football/teams/121.png",
    "Corinthians": "https://media.api-sports.io/football/teams/131.png",
    "Vasco": "https://media.api-sports.io/football/teams/133.png",
}

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

for nome, url in escudos.items():
    cursor.execute(
        "UPDATE times SET escudo = ? WHERE nome = ?",
        (url, nome)
    )

conn.commit()
conn.close()

print("Escudos atualizados com sucesso!")
