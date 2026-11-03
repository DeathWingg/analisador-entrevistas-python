# 🔍 Analisador de Entrevistas (Pesquisa Qualitativa)

Uma alternativa simplificada e gratuita ao software NVivo, desenvolvida para auxiliar estudantes e pesquisadores na análise de conteúdo de entrevistas qualitativas.

## 🎯 O problema que ele resolve
A análise de dados qualitativos (como entrevistas) exige que o pesquisador leia o texto e agrupe trechos em "categorias" ou "códigos". Ferramentas como o NVivo são caras. Este sistema oferece o essencial: cadastrar entrevistas, destacar trechos com o mouse, gerar relatórios agrupados e exportar os dados.

## 🛠️ Tecnologias utilizadas
- **Python (Flask)**: Roteamento do servidor e API REST.
- **SQLite**: Banco de dados relacional.
- **HTML / CSS**: Interface visual limpa e responsiva.
- **JavaScript (Vanilla)**: Lógica de seleção de texto e envio assíncrono de dados (Fetch API).

## ⚙️ Funcionalidades
- Cadastro de entrevistas.
- Criação de códigos de análise.
- Seleção de trechos com o mouse para aplicar um código.
- Dashboard com contadores automáticos.
- Relatório final agrupando trechos por código.
- Exportação do relatório final para CSV/Excel.

## 🚀 Como rodar o projeto

**Passo 1: Clone o repositório**
    git clone https://github.com/DeathWingg/analisador-entrevistas-python.git

**Passo 2: Crie um ambiente virtual (opcional)**
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
    ├── schema.sql            # Estrutura do banco SQLite
    ├── requirements.txt      # Dependências
    │
    ├── static/
    │   ├── css/style.css     # Estilização
    │   └── js/script.js      # Lógica de seleção
    │
    └── templates/
        ├── base.html         # Layout padrão
        ├── index.html        # Dashboard
        ├── nova_entrevista.html
        ├── entrevista.html   # Tela de leitura
        └── resultados.html   # Relatório final

---
*Desenvolvido por [Wallysson Costa](https://github.com/DeathWingg)*
