# 🚗 Sistema de Pesquisa de Satisfação - VW Capivari

![Status do Projeto](https://img.shields.io/badge/Status-Concluído%20e%20Em%20Produção-success)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey)
![Railway](https://img.shields.io/badge/Deploy-Railway-black)

## 📌 Sobre o Projeto
Este sistema foi desenvolvido como parte do **Projeto Integrador (PI)** com foco em otimizar o tempo de resposta do pós-venda da concessionária **VW Capivari**. 

O problema original consistia na demora entre a insatisfação do cliente e a ação do gerente. Para solucionar isso, criamos uma aplicação web responsiva que coleta o feedback do cliente logo após o atendimento e toma decisões automatizadas com base nas respostas.

### 🌐 Link de Produção (Online)
**Acesse o sistema rodando na nuvem:** [https://pi-vwcapivari.up.railway.app/](https://pi-vwcapivari.up.railway.app/)
=======
---

## ✨ Principais Funcionalidades

1. **Formulário de Feedback Inteligente:**
   * Coleta de dados como: Placa, Consultor, Motivo da Visita e Probabilidade de Retorno.
   * Ocultação/exibição dinâmica de campos (ex: se o problema não foi resolvido, um campo extra para explicar o motivo é exibido).

2. **Gatilho de Alerta via WhatsApp (Em Tempo Real):**
   * **Regra de Negócio:** Se o cliente responder que o problema **"Não"** foi resolvido OU se a probabilidade de retorno for **menor ou igual a 50%**, o sistema dispara um alerta imediato para o WhatsApp do gerente.
   * Integração feita utilizando a API do *CallMeBot*.

3. **Painel de Controle Administrativo (Dashboard):**
   * Tela de login segura para a gerência.
   * Visualização em tabela de todas as respostas coletadas.

---

## 🛠️ Tecnologias Utilizadas

**Backend:**
* **Python:** Linguagem principal do servidor.
* **Flask:** Framework web para gerenciamento de rotas e requisições HTTP.
* **SQLAlchemy:** ORM utilizado para gerenciar o Banco de Dados.
* **Requests / urllib:** Bibliotecas para integração com a API externa do WhatsApp.
* **Gunicorn:** Servidor WSGI utilizado para rodar a aplicação em ambiente de produção.

**Frontend:**
* **HTML5 & CSS3:** Estruturação e estilização focadas na identidade visual da marca.
* **JavaScript:** Manipulação do DOM e requisições assíncronas (Fetch API) para envio do formulário sem recarregar a página.

**Infraestrutura e Deploy:**
* **Railway:** Plataforma de cloud hosting para colocar a aplicação no ar.
* **Git & GitHub:** Versionamento de código.
* **Banco de Dados:** PostgreSQL (Nuvem/Railway) e SQLite (Ambiente de Desenvolvimento Local).

---

## ⚙️ Como Executar Localmente

Siga a sequência de comandos abaixo no seu terminal para configurar e rodar o projeto na sua máquina:

```bash
# 1. Clone o repositório e entre na pasta do projeto
git clone [https://github.com/SEU-USUARIO/nome-do-repositorio.git](https://github.com/SEU-USUARIO/nome-do-repositorio.git)
cd nome-do-repositorio

# 2. Crie o ambiente virtual (venv)
python -m venv venv

# 3. Ative o ambiente virtual
# -> Se estiver no Windows:
venv\Scripts\activate
# -> Se estiver no Mac/Linux:
source venv/bin/activate

# 4. Instale as dependências do projeto
pip install -r requirements.txt

# 5. Inicie o servidor local
python app.py

Acesse em: http://localhost:8080