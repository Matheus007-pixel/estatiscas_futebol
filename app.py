import sqlite3
import os
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from services.football_api import FootballAPI




# =====================
# Configurações iniciais
# =====================
load_dotenv()

API_KEY = os.getenv("API_FOOTBALL_KEY")

football_api = FootballAPI(API_KEY)

app = Flask(__name__)

# =====================
# Banco de dados
# =====================
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def obter_escudo_com_cache(nome_time):
        conn = get_db_connection()

        # 1️⃣ Verifica se já existe escudo no banco
        row = conn.execute(
            "SELECT escudo FROM times WHERE nome = ?",
            (nome_time,)
        ).fetchone()

        if row and row["escudo"]:
            conn.close()
            return row["escudo"]  # 🔥 CACHE HIT

        conn.close()

        # 2️⃣ Se não existir, busca na API
        escudo_api = football_api.buscar_escudo_time(nome_time)

        return escudo_api

# =====================
# Rotas
# =====================
@app.route("/")
def home():
    conn = get_db_connection()
    times = conn.execute("SELECT * FROM times").fetchall()
    conn.close()
    return render_template("index.html", times=times)

# =====================
# Cadastrar Time
# =====================
@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        nome = request.form["nome"]
        jogos = request.form["jogos"]
        gols = request.form["gols"]

        # 🔥 BUSCA AUTOMÁTICA DO ESCUDO
        escudo = obter_escudo_com_cache(nome)


        conn = get_db_connection()
        conn.execute(
            "INSERT INTO times (nome, jogos, gols, escudo) VALUES (?, ?, ?, ?)",
            (nome, jogos, gols, escudo)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("home"))

    return render_template("cadastrar.html")



# =====================
# Excluir Time
# =====================
@app.route("/excluir/<int:id>")
def excluir(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM times WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))

# =====================
# Editar Time
# =====================
@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    conn = get_db_connection()
    time = conn.execute("SELECT * FROM times WHERE id = ?", (id,)).fetchone()

    if request.method == "POST":
        nome = request.form["nome"]
        jogos = request.form["jogos"]
        gols = request.form["gols"]

        conn.execute(
            """
            UPDATE times
            SET nome = ?, jogos = ?, gols = ?
            WHERE id = ?
            """,
            (nome, jogos, gols, id)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("home"))

    conn.close()
    return render_template("editar.html", time=time)

# =====================
# Página individual do time
# =====================
@app.route("/time/<int:id>")
def time(id):
    conn = get_db_connection()
    time = conn.execute(
        "SELECT * FROM times WHERE id = ?", (id,)
    ).fetchone()
    conn.close()

    return render_template("time.html", time=time)

# =====================
# Run
# =====================
if __name__ == "__main__":
    app.run(debug=True)
