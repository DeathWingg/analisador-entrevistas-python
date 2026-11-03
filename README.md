# 🔍 Analisador de Entrevistas (Pesquisa Qualitativa)

Uma alternativa simplificada e gratuita ao software NVivo, desenvolvida para auxiliar estudantes e pesquisadores na análise de conteúdo de entrevistas qualitativas.

## 🎯 O problema que ele resolve
A análise de dados qualitativos (como entrevistas e grupos focais) exige que o pesquisador leia o texto e agrupe trechos em "categorias" ou "códigos" (ex: *Renda*, *Educação*, *Gênero*). Ferramentas como o NVivo são caras e complexas. Este sistema oferece o essencial: cadastrar entrevistas, destacar trechos com o mouse e gerar relatórios agrupados.

## 🛠️ Tecnologias utilizadas
- **Python (Flask)**: Roteamento do servidor e API REST.
- **SQLite**: Banco de dados relacional para salvar entrevistas, códigos e trechos.
- **HTML / CSS**: Interface visual limpa e responsiva.
- **JavaScript (Vanilla)**: Lógica de seleção de texto e envio assíncrono de dados (Fetch API).

## ⚙️ Funcionalidades
- Cadastro de entrevistas (título e texto completo).
- Criação de códigos de análise (categorias).
- Seleção de trechos do texto com o mouse para aplicar um código.
- Dashboard com contagem automática de entrevistas, códigos e trechos.
- Relatório final agrupando todos os trechos por código de análise.

## 🚀 Como rodar o projeto

**Passo 1: Clone o repositório**
    git clone https://github.com/DeathWingg/analisador-entrevistas-python.git

**Passo 2: Crie um ambiente virtual (opcional, mas recomendado)**
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate

**Passo 3: Instale as dependências**
    pip install -r requirements.txt

**Passo 4: Execute o servidor**
    python app.py

O sistema estará disponível em: `http://127.0.0.1:5000`

## 📁 Estrutura do projeto

    analisador-entrevistas-python/
    │
    ├── app.py                # Servidor Flask e rotas
    ├── schema.sql            # Estrutura do banco de dados SQLite
    ├── requirements.txt      # Dependências do projeto
    │
    ├── static/
    │   ├── css/style.css     # Estilização da interface
    │   └── js/script.js      # Lógica de seleção de texto
    │
    └── templates/
        ├── base.html         # Layout padrão
        ├── index.html        # Dashboard principal
        ├── nova_entrevista.html
        ├── entrevista.html   # Tela de leitura
        └── resultados.html   # Relatório final

---
*Desenvolvido por [Wallysson Costa](https://github.com/DeathWingg)*
