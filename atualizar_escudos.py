import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

dados = [
    ("flamengo.png", "Flamengo"),
    ("palmeiras.png", "Palmeiras"),
    ("corinthians.png", "Corinthians"),
    ("santos.png", "Santos"),
    ("saopaulo.png", "São Paulo"),
    ("vasco.png", "Vasco")
]

cursor.executemany(
    "UPDATE times SET escudo = ? WHERE nome = ?",
    dados
)

conn.commit()
conn.close()

print("escudos atualizados!")
