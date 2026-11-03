from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DATABASE = "database.db"


def init_db():
    if not os.path.exists(DATABASE):
        with sqlite3.connect(DATABASE) as conn:
            with open("schema.sql", "r", encoding="utf-8") as f:
                conn.executescript(f.read())
        print("✅ Banco de dados inicializado!")


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    conn = get_db()
    # Conta quantas entrevistas existem no banco
    total_entrevistas = conn.execute("SELECT COUNT(*) FROM entrevistas").fetchone()[0]
    conn.close()
    return render_template("index.html", total_entrevistas=total_entrevistas)


@app.route("/nova_entrevista", methods=("GET", "POST"))
def nova_entrevista():
    if request.method == "POST":
        titulo = request.form["titulo"]
        texto = request.form["texto"]

        conn = get_db()
        conn.execute(
            "INSERT INTO entrevistas (titulo, texto) VALUES (?, ?)", (titulo, texto)
        )
        conn.commit()
        conn.close()

        # Depois de salvar, volta para o painel principal
        return redirect(url_for("index"))

    return render_template("nova_entrevista.html")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
