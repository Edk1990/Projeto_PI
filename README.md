# Formulário de Pesquisa de Satisfação

Este é um projeto de aplicação web desenvolvido em Python com o framework Flask. O objetivo da aplicação é coletar feedback de satisfação de clientes através de um formulário online e apresentar os resultados em um painel administrativo.

## Funcionalidades

- **Formulário de Pesquisa:** Uma interface simples para os clientes preencherem suas informações e feedback.
- **Painel Administrativo:** Uma área restrita por login onde é possível visualizar todas as respostas enviadas.
- **Banco de Dados:** Utiliza SQLite para desenvolvimento local e é configurado para usar PostgreSQL em produção (Heroku).

## Tecnologias Utilizadas

- **Backend:**
  - Python 3.8+
  - Flask
  - Flask-SQLAlchemy
  - Gunicorn (para produção)

- **Frontend:**
  - HTML
  - CSS
  - JavaScript

- **Banco de Dados:**
  - SQLite (Desenvolvimento)
  - PostgreSQL (Produção)

## Como Executar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Edk1990/Projeto_PI.git
   cd Projeto_PI
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   # No Windows
   py -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**
   ```bash
   py app.py
   ```

   A aplicação estará disponível em `http://127.0.0.1:5000`.

## Deploy no Heroku

O projeto está configurado para deploy na plataforma Heroku. As instruções detalhadas para o deploy podem ser encontradas na documentação do Heroku, mas os arquivos necessários (`Procfile`, `runtime.txt`) já estão incluídos.
