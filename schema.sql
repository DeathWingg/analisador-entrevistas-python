CREATE TABLE IF NOT EXISTS entrevistas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    texto TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS codigos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cor TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS trechos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_entrevista INTEGER NOT NULL,
    id_codigo INTEGER NOT NULL,
    texto_selecionado TEXT NOT NULL,
    posicao_inicial INTEGER NOT NULL,
    posicao_final INTEGER NOT NULL,
    FOREIGN KEY (id_entrevista) REFERENCES entrevistas (id),
    FOREIGN KEY (id_codigo) REFERENCES codigos (id)
);