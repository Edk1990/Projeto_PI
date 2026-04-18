# Projeto PI - Sistema de Pesquisa de Satisfação

## Descrição

Sistema web para coleta e análise de pesquisas de satisfação de clientes, desenvolvido em Flask com banco de dados PostgreSQL/SQLite. O projeto permite que clientes respondam a pesquisas e que administradores visualizem e exportem os resultados.

## Funcionalidades

- 📝 **Formulário de Pesquisa**: Interface responsiva para coleta de respostas dos clientes
- 🔐 **Painel Administrativo**: Dashboard para visualização e gerenciamento de dados
- 📊 **Exportação de Dados**: Geração de relatórios em Excel e CSV
- 🌐 **Deploy Multiplataforma**: Suporte para Railway, Render e outros serviços
- ♿ **Acessibilidade**: Interface seguindo boas práticas de acessibilidade

## Tecnologias Utilizadas

- **Backend**: Flask 3.0.0
- **Banco de Dados**: PostgreSQL (produção) / SQLite (desenvolvimento)
- **ORM**: SQLAlchemy 3.1.1
- **Deploy**: Gunicorn 22.0.0
- **Frontend**: HTML5, CSS3, JavaScript
- **Bibliotecas Adicionais**:
  - python-dotenv (gerenciamento de variáveis de ambiente)
  - psycopg2-binary (conector PostgreSQL)

## Estrutura do Projeto

```
Projeto_PI/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências Python
├── templates/            # Arquivos HTML
│   ├── tela_perguntas.html
│   ├── dashboard_admin.html
│   ├── tela_login_admin.html
│   └── ...
├── assets/               # Arquivos estáticos (CSS, JS, imagens)
├── routes/               # Rotas da aplicação
├── Formulario/           # Componentes do formulário
└── docs/                 # Documentação
```

## Instalação e Configuração

### Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)
- Git

### Passos para Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Edk1990/Projeto_PI.git
   cd Projeto_PI
   ```

2. **Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente** (opcional):
   ```bash
   # Para desenvolvimento local, o SQLite será usado automaticamente
   # Para produção, configure DATABASE_URL para PostgreSQL
   export DATABASE_URL=postgresql://usuario:senha@host:porta/database
   ```

5. **Execute a aplicação**:
   ```bash
   python app.py
   ```

6. **Acesse a aplicação**:
   - Formulário de pesquisa: `http://localhost:5000`
   - Painel administrativo: `http://localhost:5000/admin`

   **Credenciais do administrador**:
   - Email: `admin`
   - Senha: `admin`

## Deploy

### Railway

1. Faça o deploy da branch `main` para o Railway
2. Configure a variável de ambiente `DATABASE_URL`
3. A aplicação estará disponível na URL fornecida pelo Railway

### Render

1. Conecte seu repositório GitHub ao Render
2. Configure para fazer deploy da branch `main`
3. Adicione a variável de ambiente `DATABASE_URL`
4. A aplicação será implantada automaticamente

*Para instruções detalhadas, consulte os arquivos `DEPLOY_RAILWAY.md` e `DEPLOY_RENDER.md`.*

## API

A aplicação oferece endpoints REST para integração:

- `POST /api/respostas` - Salvar nova resposta
- `GET /api/respostas` - Listar todas as respostas
- `GET /api/exportar/excel` - Exportar dados em Excel
- `GET /api/exportar/csv` - Exportar dados em CSV

*Documentação completa disponível em `API_DOCUMENTATION.md`.*

## Acessibilidade

O projeto segue as diretrizes WCAG 2.1 de acessibilidade:

- HTML semântico adequado
- Navegação por teclado
- Contraste de cores adequado
- Textos alternativos para imagens
- Estrutura de cabeçalhos lógica

*Mais informações em `ACESSIBILIDADE.md` e `GUIA_RAPIDO_ACESSIBILIDADE.md`.*

## Desenvolvimento

### Branches

- `main` - Versão de produção
- `Alpha` - Branch de testes e desenvolvimento

### Como Contribuir

1. Crie uma branch para sua feature: `git checkout -b nome-da-feature`
2. Faça commit das suas alterações: `git commit -m 'Descrição da alteração'`
3. Push para a branch: `git push origin nome-da-feature`
4. Abra um Pull Request para a branch `main`

## Licença

Este projeto está sob licença MIT. Consulte o arquivo LICENSE para mais informações.

## Contato

Desenvolvido por [Eduardo K](https://github.com/Edk1990)

---

**Nota**: Este é um projeto acadêmico desenvolvido como parte do Projeto Integrador.
