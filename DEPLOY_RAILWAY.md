# 🚀 Guia de Deploy no Railway

## Pré-requisitos
- Conta no GitHub (para conectar o repositório)
- Conta no Railway (https://railway.app)

## Passo 1: Preparar o Repositório Git

### 1.1 Verificar se Git está inicializado
```powershell
cd "c:\Users\Eduardo K\Documents\GitHub\Projeto_PI"
git status
```

### 1.2 Se não estiver inicializado, execute:
```powershell
git init
git add .
git commit -m "Preparando deploy para Railway"
```

### 1.3 Conectar ao GitHub
```powershell
# Substitua 'seu-usuario' pelo seu username do GitHub
git remote add origin https://github.com/seu-usuario/Projeto_PI.git
git branch -M main
git push -u origin main
```

**Se o repositório não existir no GitHub:**
1. Acesse: https://github.com/new
2. Crie um repositório chamado `Projeto_PI`
3. **NÃO** marque "Initialize with README"
4. Execute os comandos acima

---

## Passo 2: Criar Projeto no Railway

### 2.1 Acessar Railway
1. Vá para: https://railway.app
2. Clique em **"Login"**
3. Faça login com sua conta GitHub

### 2.2 Criar Novo Projeto
1. Clique em **"New Project"**
2. Selecione **"Deploy from GitHub repo"**
3. Se for a primeira vez, autorize o Railway a acessar seus repositórios
4. Selecione o repositório **"Projeto_PI"**

### 2.3 Confirmar Deploy
- O Railway detectará automaticamente que é um projeto Python Flask
- Clique em **"Deploy Now"**

---

## Passo 3: Adicionar PostgreSQL

### 3.1 Adicionar Banco de Dados
1. No dashboard do projeto, clique em **"+ New"**
2. Selecione **"Database"**
3. Escolha **"Add PostgreSQL"**

### 3.2 Conectar ao Serviço
1. O Railway criará automaticamente a variável `DATABASE_URL`
2. Seu código já está configurado para usar essa variável!

---

## Passo 4: Configurar Variáveis de Ambiente (Opcional)

Se precisar adicionar variáveis personalizadas:

1. Clique no serviço da aplicação (não no banco)
2. Vá em **"Variables"**
3. Adicione variáveis conforme necessário

**Exemplo:**
```
FLASK_ENV=production
SECRET_KEY=sua-chave-secreta-aqui
```

---

## Passo 5: Acessar a Aplicação

### 5.1 Obter URL Pública
1. Clique no serviço da aplicação
2. Vá em **"Settings"**
3. Role até **"Domains"**
4. Clique em **"Generate Domain"**

A URL será algo como: `https://projeto-pi-production.up.railway.app`

### 5.2 Testar
Acesse a URL gerada no navegador!

---

## 📋 Checklist de Verificação

- [ ] Repositório Git inicializado
- [ ] Código enviado para GitHub
- [ ] Projeto criado no Railway
- [ ] PostgreSQL adicionado
- [ ] Deploy concluído com sucesso
- [ ] Domínio gerado
- [ ] Aplicação acessível na URL

---

## 🔄 Atualizações Futuras

Para atualizar a aplicação após mudanças no código:

```powershell
git add .
git commit -m "Descrição da mudança"
git push origin main
```

O Railway fará o deploy automático! 🎉

---

## 🆘 Solução de Problemas

### Erro de Build
- Verifique os logs no Railway (aba "Deployments")
- Confirme que `requirements.txt` está correto

### Erro de Conexão com Banco
- Verifique se o PostgreSQL foi adicionado
- Confirme que a variável `DATABASE_URL` existe em "Variables"

### Aplicação não inicia
- Verifique se o `Procfile` está correto
- Confirme que `gunicorn` está no `requirements.txt`

---

## 💰 Plano Gratuito

O Railway oferece:
- **$5 de crédito/mês gratuitamente**
- Suficiente para aplicações pequenas/médias
- PostgreSQL incluído no crédito

**Dica:** Monitore o uso em "Usage" no dashboard

---

## 📞 Suporte

- Documentação: https://docs.railway.app
- Discord: https://discord.gg/railway
