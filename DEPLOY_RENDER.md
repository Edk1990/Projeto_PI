# 🚀 Deploy no Render.com

## Por que Render?
- ✅ **Mais estável que Railway**
- ✅ **750 horas gratuitas/mês**
- ✅ **PostgreSQL gratuito incluído**
- ✅ **Sem problemas de cache**
- ✅ **Deploy automático do GitHub**

---

## Passo a Passo Completo

### 1. Criar Conta no Render

1. Acesse: https://render.com
2. Clique em **"Get Started for Free"**
3. Faça login com sua **conta GitHub**
4. Autorize o Render a acessar seus repositórios

---

### 2. Criar Banco de Dados PostgreSQL

1. No dashboard, clique em **"New +"**
2. Selecione **"PostgreSQL"**
3. Configure:
   - **Name:** `capivari-pesquisa-db`
   - **Database:** `pesquisa`
   - **User:** `pesquisa_user`
   - **Region:** Escolha o mais próximo (ex: Ohio)
   - **Plan:** **Free** (gratuito)
4. Clique em **"Create Database"**
5. ⏳ Aguarde ~2 minutos até ficar "Available"
6. **Copie a "Internal Database URL"** (vai usar depois)

---

### 3. Criar Web Service

1. No dashboard, clique em **"New +"**
2. Selecione **"Web Service"**
3. Conecte ao GitHub:
   - Se primeira vez, autorize o Render
   - Selecione o repositório: **"Edk1990/Projeto_PI"**
4. Configure o serviço:

**Configurações Básicas:**
- **Name:** `capivari-pesquisa-satisfacao`
- **Region:** Mesmo do banco de dados
- **Branch:** `main`
- **Root Directory:** (deixe em branco)
- **Runtime:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

**Environment Variables (Variáveis de Ambiente):**
- Clique em **"Add Environment Variable"**
- **Key:** `DATABASE_URL`
- **Value:** Cole a "Internal Database URL" do PostgreSQL que você copiou

**Plano:**
- Selecione **"Free"** (gratuito)

5. Clique em **"Create Web Service"**

---

### 4. Aguardar Deploy

1. O Render iniciará o build automaticamente
2. Você verá os logs em tempo real
3. ⏳ Aguarde ~5 minutos
4. Quando aparecer **"Your service is live 🎉"**, está pronto!

---

### 5. Acessar Aplicação

1. No topo da página, você verá a URL do serviço
2. Será algo como: `https://capivari-pesquisa-satisfacao.onrender.com`
3. Clique e teste!

---

## 🔄 Atualizações Futuras

Sempre que você fizer push para o GitHub (branch main):
```bash
git add .
git commit -m "Sua mensagem"
git push origin main
```

O Render fará **redeploy automático**! 🎉

---

## ⚙️ Configurações Opcionais

### Adicionar Domínio Customizado
1. Settings → Custom Domains
2. Adicione seu domínio (se tiver)

### Ver Logs
- Na página do serviço, clique em **"Logs"**
- Logs em tempo real

### Reiniciar Serviço
- Settings → Manual Deploy → **"Clear build cache & deploy"**

---

## 🆘 Troubleshooting

### Erro: "Failed to bind to $PORT"
- Verifique se o start command está: `gunicorn app:app`

### Erro: "No module named 'psycopg2'"
- Verifique se `psycopg2-binary` está no `requirements.txt`

### Banco de dados não conecta
- Verifique se a variável `DATABASE_URL` foi configurada
- Copie novamente a Internal Database URL

### Aplicação está lenta
- Render Free dorme após 15 min de inatividade
- Primeira requisição demora ~30s (wake up)

---

## 💰 Plano Gratuito

- **750 horas/mês** de runtime (suficiente para 1 app 24/7)
- **PostgreSQL com 1GB** de armazenamento
- **100GB de banda** por mês
- Aplicação "dorme" após 15 min sem uso

---

## ✅ Checklist Final

- [ ] Conta Render criada e conectada ao GitHub
- [ ] PostgreSQL criado e rodando
- [ ] Web Service criado e conectado ao repo
- [ ] Variável `DATABASE_URL` configurada
- [ ] Deploy concluído com sucesso
- [ ] Aplicação acessível via URL

---

## 🎯 Vantagens vs Railway

| Recurso | Render | Railway |
|---------|--------|---------|
| Cache Issues | ✅ Nenhum | ❌ Persistentes |
| Plano Grátis | ✅ 750h/mês | ⚠️ $5 crédito/mês |
| PostgreSQL | ✅ Gratuito | ⚠️ Limitado |
| Estabilidade | ✅ Alta | ⚠️ Média |
| Interface | ✅ Simples | ✅ Moderna |

---

**Pronto para o deploy no Render? Siga os passos acima!** 🚀
