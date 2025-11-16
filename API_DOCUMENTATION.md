# 📋 Documentação da API v1 - Sistema de Pesquisa de Satisfação

## Base URL
```
http://localhost:5000/api/v1
```

---

## 🔐 Autenticação
Atualmente a API não requer token de autenticação para consultas. O endpoint DELETE requer validação administrativa (a ser implementado via frontend).

---

## 📍 Endpoints Disponíveis

### 1. **Listar Todas as Respostas**
Retorna todas as respostas da pesquisa com filtros opcionais.

**Endpoint:** `GET /api/v1/respostas`

**Query Parameters (Opcionais):**
- `consultor` - Filtrar por nome do consultor (busca parcial, case-insensitive)
- `data_inicio` - Filtrar por data inicial (formato: YYYY-MM-DD)
- `data_fim` - Filtrar por data final (formato: YYYY-MM-DD)

**Exemplo de Request:**
```bash
GET /api/v1/respostas?consultor=João&data_inicio=2025-01-01&data_fim=2025-12-31
```

**Response (200 OK):**
```json
{
  "success": true,
  "total": 2,
  "data": [
    {
      "id": 1,
      "email": "cliente@email.com",
      "data_visita": "2025-05-25",
      "placa": "ABC-1234",
      "consultor": "João Silva",
      "motivo_visita": "Manutenção",
      "problema_resolvido": "Sim",
      "problema_nao_resolvido": "",
      "sugestoes": "Ótimo atendimento",
      "probability": 10,
      "data_resposta": "2025-05-25 14:30:00"
    }
  ]
}
```

---

### 2. **Buscar Resposta por ID**
Retorna uma resposta específica.

**Endpoint:** `GET /api/v1/respostas/{id}`

**Path Parameters:**
- `id` - ID da resposta (integer)

**Exemplo de Request:**
```bash
GET /api/v1/respostas/1
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "email": "cliente@email.com",
    "data_visita": "2025-05-25",
    "placa": "ABC-1234",
    "consultor": "João Silva",
    "motivo_visita": "Manutenção",
    "problema_resolvido": "Sim",
    "problema_nao_resolvido": "",
    "sugestoes": "Ótimo atendimento",
    "probability": 10,
    "data_resposta": "2025-05-25 14:30:00"
  }
}
```

**Response (404 Not Found):**
```json
{
  "success": false,
  "error": "Resposta não encontrada"
}
```

---

### 3. **Deletar Resposta**
Remove uma resposta específica do banco de dados.

**Endpoint:** `DELETE /api/v1/respostas/{id}`

**Path Parameters:**
- `id` - ID da resposta (integer)

**Exemplo de Request:**
```bash
DELETE /api/v1/respostas/1
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Resposta ID 1 deletada com sucesso"
}
```

**Response (404 Not Found):**
```json
{
  "success": false,
  "error": "Resposta não encontrada"
}
```

---

### 4. **Obter Estatísticas**
Retorna métricas e estatísticas gerais das pesquisas.

**Endpoint:** `GET /api/v1/estatisticas`

**Exemplo de Request:**
```bash
GET /api/v1/estatisticas
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "total_respostas": 150,
    "nps_medio": 8.5,
    "problemas": {
      "resolvidos": 140,
      "nao_resolvidos": 10,
      "taxa_resolucao": 93.33
    },
    "nps_distribuicao": {
      "detratores": 15,
      "neutros": 30,
      "promotores": 105
    },
    "consultores": [
      {
        "nome": "João Silva",
        "total_atendimentos": 45,
        "nps_medio": 9.2
      },
      {
        "nome": "Maria Santos",
        "total_atendimentos": 38,
        "nps_medio": 8.8
      }
    ]
  }
}
```

**Descrição dos Campos:**
- **total_respostas** - Total de pesquisas respondidas
- **nps_medio** - Média geral de NPS (0-10)
- **problemas.resolvidos** - Quantidade de problemas resolvidos
- **problemas.nao_resolvidos** - Quantidade de problemas não resolvidos
- **problemas.taxa_resolucao** - Percentual de resolução
- **nps_distribuicao.detratores** - Clientes com NPS 0-6
- **nps_distribuicao.neutros** - Clientes com NPS 7-8
- **nps_distribuicao.promotores** - Clientes com NPS 9-10
- **consultores** - Desempenho individual de cada consultor

---

### 5. **Exportar para CSV**
Gera e baixa um arquivo CSV com todas as respostas.

**Endpoint:** `GET /api/v1/export/csv`

**Exemplo de Request:**
```bash
GET /api/v1/export/csv
```

**Response:**
- Arquivo CSV (.csv) para download

**Arquivo CSV Contém:**
- ID
- Email
- Data Visita
- Placa
- Consultor
- Motivo Visita
- Problema Resolvido
- Problema Não Resolvido
- Sugestões
- NPS (0-10)
- Data Resposta

---

## 🔄 Endpoints Antigos (Compatibilidade)

Os endpoints abaixo continuam funcionando normalmente:

- `POST /submit` - Submeter pesquisa (frontend)
- `POST /admin/login` - Login do administrador
- `GET /admin/respostas` - Listar respostas (formato antigo)

---

## 📊 Códigos de Status HTTP

| Código | Descrição |
|--------|-----------|
| 200 | Sucesso |
| 404 | Recurso não encontrado |
| 500 | Erro interno do servidor |

---

## 🧪 Exemplos de Uso

### Usando cURL

**Listar todas as respostas:**
```bash
curl -X GET http://localhost:5000/api/v1/respostas
```

**Buscar resposta específica:**
```bash
curl -X GET http://localhost:5000/api/v1/respostas/1
```

**Obter estatísticas:**
```bash
curl -X GET http://localhost:5000/api/v1/estatisticas
```

**Deletar resposta:**
```bash
curl -X DELETE http://localhost:5000/api/v1/respostas/1
```

**Baixar CSV:**
```bash
curl -X GET http://localhost:5000/api/v1/export/csv -o relatorio.csv
```

### Usando JavaScript (Fetch API)

```javascript
// Listar respostas com filtro
fetch('http://localhost:5000/api/v1/respostas?consultor=João')
  .then(response => response.json())
  .then(data => console.log(data));

// Obter estatísticas
fetch('http://localhost:5000/api/v1/estatisticas')
  .then(response => response.json())
  .then(data => console.log(data));

// Deletar resposta
fetch('http://localhost:5000/api/v1/respostas/1', {
  method: 'DELETE'
})
  .then(response => response.json())
  .then(data => console.log(data));

// Download CSV
fetch('http://localhost:5000/api/v1/export/csv')
  .then(response => response.blob())
  .then(blob => {
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'relatorio.csv';
    a.click();
  });
```

### Usando Python (requests)

```python
import requests

# Listar respostas
response = requests.get('http://localhost:5000/api/v1/respostas')
print(response.json())

# Obter estatísticas
response = requests.get('http://localhost:5000/api/v1/estatisticas')
print(response.json())

# Deletar resposta
response = requests.delete('http://localhost:5000/api/v1/respostas/1')
print(response.json())

# Download CSV
response = requests.get('http://localhost:5000/api/v1/export/csv')
with open('relatorio.csv', 'wb') as f:
    f.write(response.content)
```

---

## 🚀 Como Testar

1. **Iniciar o servidor:**
```bash
python app.py
```

2. **Testar no navegador:**
- Estatísticas: http://localhost:5000/api/v1/estatisticas
- Listar todas: http://localhost:5000/api/v1/respostas
- Exportar CSV: http://localhost:5000/api/v1/export/csv

3. **Testar com Postman/Insomnia:**
- Importe os endpoints acima
- Configure a base URL: `http://localhost:5000/api/v1`

---

## ⚠️ Notas Importantes

1. **Segurança:** O endpoint DELETE atualmente não tem autenticação. Recomenda-se adicionar validação de token/sessão admin antes de usar em produção.

2. **Filtros:** Os filtros de data usam comparação direta. Certifique-se de usar o formato correto (YYYY-MM-DD).

3. **Excel:** O arquivo é gerado em memória e não é salvo no servidor.

4. **NPS:** A distribuição de NPS segue o padrão:
   - Detratores: 0-6
   - Neutros: 7-8
   - Promotores: 9-10

5. **Compatibilidade:** Todos os endpoints antigos continuam funcionando. A API v1 é uma adição, não uma substituição.

---

## 📝 Changelog

### v1.0.0 (2025-11-16)
- ✅ Endpoint GET /api/v1/respostas (com filtros)
- ✅ Endpoint GET /api/v1/respostas/{id}
- ✅ Endpoint DELETE /api/v1/respostas/{id}
- ✅ Endpoint GET /api/v1/estatisticas
- ✅ Endpoint GET /api/v1/export/csv
- ✅ Versionamento de API implementado
- ✅ Compatibilidade 100% com código existente mantida
