from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
import sqlite3
import os
import csv
import io

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
    # Contadores do dashboard
    total_entrevistas = conn.execute("SELECT COUNT(*) FROM entrevistas").fetchone()[0]
    total_codigos = conn.execute("SELECT COUNT(*) FROM codigos").fetchone()[0]
    total_trechos = conn.execute("SELECT COUNT(*) FROM trechos").fetchone()[0]

    # Lista de entrevistas cadastradas
    entrevistas = conn.execute("SELECT * FROM entrevistas ORDER BY id DESC").fetchall()
    conn.close()

    return render_template(
        "index.html",
        total_entrevistas=total_entrevistas,
        total_codigos=total_codigos,
        total_trechos=total_trechos,
        entrevistas=entrevistas,
    )


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
        return redirect(url_for("index"))
    return render_template("nova_entrevista.html")


@app.route("/entrevista/<int:id>")
def ver_entrevista(id):
    conn = get_db()
    entrevista = conn.execute(
        "SELECT * FROM entrevistas WHERE id = ?", (id,)
    ).fetchone()
    codigos = conn.execute("SELECT * FROM codigos").fetchall()
    conn.close()
    return render_template("entrevista.html", entrevista=entrevista, codigos=codigos)


@app.route("/novo_codigo", methods=["POST"])
def novo_codigo():
    nome = request.form["nome"]
    cor = "#e74c3c"  # Cor padrão para os códigos
    conn = get_db()
    conn.execute("INSERT INTO codigos (nome, cor) VALUES (?, ?)", (nome, cor))
    conn.commit()
    conn.close()
    return redirect(request.referrer or url_for("index"))


@app.route("/salvar_trecho", methods=["POST"])
def salvar_trecho():
    data = request.json
    conn = get_db()
    conn.execute(
        "INSERT INTO trechos (id_entrevista, id_codigo, texto_selecionado, posicao_inicial, posicao_final) VALUES (?, ?, ?, ?, ?)",
        (
            data["id_entrevista"],
            data["id_codigo"],
            data["texto"],
            data["inicio"],
            data["fim"],
        ),
    )
    conn.commit()
    conn.close()
    return jsonify({"status": "sucesso"})


@app.route("/resultados")
def resultados():
    conn = get_db()
    codigos = conn.execute("SELECT * FROM codigos").fetchall()
    relatorio = []

    for c in codigos:
        # Busca todos os trechos que usam esse código e junta com o título da entrevista
        trechos = conn.execute(
            """
            SELECT t.texto_selecionado, e.titulo 
            FROM trechos t
            JOIN entrevistas e ON t.id_entrevista = e.id
            WHERE t.id_codigo = ?
        """,
            (c["id"],),
        ).fetchall()

        relatorio.append({"codigo": c["nome"], "trechos": trechos})

    conn.close()
    return render_template("resultados.html", relatorio=relatorio)


@app.route("/exportar_relatorio")
def exportar_relatorio():
    conn = get_db()
    # Pega todos os trechos com seus respectivos códigos e entrevistas
    query = """
        SELECT c.nome AS codigo, e.titulo AS entrevista, t.texto_selecionado AS trecho
        FROM trechos t
        JOIN codigos c ON t.id_codigo = c.id
        JOIN entrevistas e ON t.id_entrevista = e.id
        ORDER BY c.nome, e.titulo
    """
    dados = conn.execute(query).fetchall()
    conn.close()

    # Cria um arquivo CSV em memória
    output = io.StringIO()
    writer = csv.writer(
        output, delimiter=";"
    )  # Ponto e vírgula para abrir bonito no Excel brasileiro

    # Escreve o cabeçalho
    writer.writerow(["Código de Análise", "Entrevista", "Trecho Selecionado"])

    # Escreve os dados
    for linha in dados:
        writer.writerow([linha["codigo"], linha["entrevista"], linha["trecho"]])

    # Prepara o arquivo para download
    output.seek(0)
    return send_file(
        io.BytesIO(
            output.getvalue().encode("utf-8-sig")
        ),  # utf-8-sig para o Excel ler os acentos certinho
        mimetype="text/csv",
        as_attachment=True,
        download_name="relatorio_analise.csv",
    )


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
