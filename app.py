import sqlite3
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from services.escudos import salvar_escudo

app = Flask(__name__)
app.secret_key ="chave-secreta"

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 # 2 MB

# =====================
# Banco de dados
# =====================
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

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

        arquivo = request.files.get("escudo")
        escudo = salvar_escudo(arquivo, nome)
        if arquivo and arquivo.filename != "":
            if arquivo.mimetype not in ["image/png", "image/jpeg"]:
                flash(" Formato inválido. Envie uma imagem PNG ou JPG.")
                return redirect(url_for("cadastrar"))

            arquivo.seek(0, os.SEEK_END)
            tamanho = arquivo.tell()
            arquivo.seek(0)

            if tamanho > 2 * 1024 * 1024:
                flash(" A imagem deve ter no máximo 2 MB.")
                return redirect(url_for("cadastrar"))

        if not escudo:
            escudo = "/static/escudos/default.png"

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

    time = conn.execute(
        "SELECT escudo FROM times WHERE id = ?", (id,)
    ).fetchone()

    if time and time["escudo"] and "uploads/escudos" in time["escudo"]:
        caminho = time["escudo"].lstrip("/")
        if os.path.exists(caminho):
            os.remove(caminho)

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
