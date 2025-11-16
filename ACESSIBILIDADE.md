# 🌟 Recursos de Acessibilidade - Pesquisa de Satisfação VW Capivari

Este documento descreve os recursos de acessibilidade implementados no sistema de Pesquisa de Satisfação da Volkswagen Capivari.

## 📋 Sumário

1. [Funcionalidades Implementadas](#funcionalidades-implementadas)
2. [Modo Alto Contraste](#modo-alto-contraste)
3. [Compatibilidade com Leitores de Tela](#compatibilidade-com-leitores-de-tela)
4. [Atalhos de Teclado](#atalhos-de-teclado)
5. [Navegação por Teclado](#navegação-por-teclado)
6. [Tecnologias e Padrões](#tecnologias-e-padrões)
7. [Testes de Compatibilidade](#testes-de-compatibilidade)

---

## ✨ Funcionalidades Implementadas

### 1. **Modo Alto Contraste** 🎨
Sistema completo de temas de alto contraste para usuários com deficiência visual parcial ou daltonismo.

### 2. **Suporte a Leitores de Tela** 📢
HTML semântico e atributos WAI-ARIA para compatibilidade total com NVDA, JAWS e VoiceOver.

---

## 🎨 Modo Alto Contraste

### Como Ativar

#### Método 1: Botão Visual
- Um botão **"Alto Contraste"** aparece no canto superior direito de todas as páginas
- Clique no botão para alternar entre modo normal e alto contraste
- A preferência é salva automaticamente no navegador

#### Método 2: Atalho de Teclado
- Pressione **Alt + C** em qualquer página para ativar/desativar
- Funciona em todas as telas do sistema

### Características do Modo Alto Contraste

#### Cores Otimizadas
- **Fundo**: Preto (#000000)
- **Texto**: Branco (#FFFFFF)
- **Links**: Amarelo (#FFFF00)
- **Botões**: Amarelo com texto preto
- **Bordas**: Brancas, mais espessas (2-3px)

#### Contraste Mínimo
- Relação de contraste: **21:1** (excede WCAG AAA)
- Texto: Branco sobre preto
- Elementos interativos: Alto contraste amarelo/branco

#### Elementos Otimizados
- ✅ Inputs e formulários
- ✅ Botões e links
- ✅ Tabelas e dados
- ✅ Cartões de estatísticas
- ✅ Mensagens de erro
- ✅ Barras de progresso
- ✅ Navegação e menus

### Persistência
A preferência do usuário é salva usando `localStorage`, mantendo a escolha mesmo após fechar o navegador.

---

## 📢 Compatibilidade com Leitores de Tela

### Leitores Compatíveis
- ✅ **NVDA** (Windows)
- ✅ **JAWS** (Windows)
- ✅ **VoiceOver** (macOS/iOS)
- ✅ **TalkBack** (Android)
- ✅ **Narrator** (Windows)

### HTML Semântico Implementado

#### Tags Semânticas
```html
<main>     - Conteúdo principal
<nav>      - Navegação
<aside>    - Conteúdo complementar
<section>  - Seções de conteúdo
<article>  - Conteúdo independente
<header>   - Cabeçalhos
<form>     - Formulários
<fieldset> - Agrupamento de campos
<legend>   - Legenda de fieldsets
```

### Atributos WAI-ARIA

#### Roles
- `role="main"` - Identifica conteúdo principal
- `role="navigation"` - Áreas de navegação
- `role="form"` - Formulários
- `role="button"` - Links como botões
- `role="alert"` - Mensagens de erro
- `role="status"` - Atualizações de status
- `role="progressbar"` - Barras de progresso
- `role="table"`, `role="row"`, `role="columnheader"` - Tabelas

#### ARIA Labels
- `aria-label` - Rótulos descritivos
- `aria-labelledby` - Referência a elementos de rótulo
- `aria-describedby` - Descrições adicionais
- `aria-required` - Campos obrigatórios
- `aria-invalid` - Validação de campos

#### Live Regions
- `aria-live="polite"` - Anúncios não urgentes
- `aria-live="assertive"` - Anúncios urgentes (erros)
- `aria-atomic="true"` - Anuncia conteúdo completo

#### Estados
- `aria-pressed` - Estado de botões toggle
- `aria-sort` - Estado de ordenação em tabelas
- `aria-valuenow/min/max` - Valores de progresso

### Anúncios Automáticos

O sistema anuncia automaticamente para leitores de tela:
- ✅ Carregamento de página
- ✅ Ativação/desativação de alto contraste
- ✅ Envio de formulário com sucesso
- ✅ Erros de validação
- ✅ Mudanças na ordenação de tabelas
- ✅ Mudanças em estatísticas (dashboard)

### Labels para Todos os Inputs

Todos os campos de formulário têm:
- Labels visíveis ou `.sr-only` (screen reader only)
- Placeholders descritivos
- Mensagens de ajuda com `aria-describedby`
- Indicação clara de campos obrigatórios

---

## ⌨️ Atalhos de Teclado

### Atalhos Globais

| Atalho | Ação |
|--------|------|
| **Alt + C** | Ativar/Desativar Alto Contraste |
| **Alt + 1** | Ir para conteúdo principal |
| **Tab** | Navegar para próximo elemento |
| **Shift + Tab** | Navegar para elemento anterior |
| **Enter** | Ativar link/botão |
| **Espaço** | Ativar botão/checkbox |

### Formulários

| Tecla | Ação |
|-------|------|
| **Tab** | Próximo campo |
| **Shift + Tab** | Campo anterior |
| **Setas ↑↓** | Navegar em select/radio |
| **Espaço** | Marcar checkbox/radio |

### Tabelas (Dashboard)

| Ação | Como Fazer |
|------|------------|
| Ordenar coluna | Clicar no cabeçalho ou Enter com foco |
| Navegar células | Tab entre células |
| Ler conteúdo | Leitor de tela anuncia automaticamente |

---

## 🎯 Navegação por Teclado

### Ordem de Tabulação (Tab Order)

Todos os elementos interativos são acessíveis via Tab:
1. ✅ Links de navegação
2. ✅ Campos de formulário
3. ✅ Botões de ação
4. ✅ Elementos de tabela
5. ✅ Controles de paginação

### Skip Links

Um link "Pular para conteúdo principal" é fornecido no início de cada página (visível apenas ao focar com Tab).

### Focus Visível

Todos os elementos focados têm indicação visual clara:
- Contorno azul de 3px
- Offset de 2px para melhor visibilidade
- Visível tanto em modo normal quanto alto contraste

---

## 🔧 Tecnologias e Padrões

### Padrões Seguidos

- ✅ **WCAG 2.1 Nível AA** - Web Content Accessibility Guidelines
- ✅ **WAI-ARIA 1.2** - Web Accessibility Initiative - Accessible Rich Internet Applications
- ✅ **HTML5 Semântico** - Uso correto de elementos semânticos
- ✅ **Contraste WCAG AAA** - Relação de contraste 21:1 em alto contraste

### Arquivos Implementados

```
assets/
├── css/
│   └── accessibility.css    # Estilos de acessibilidade e alto contraste
└── js/
    └── accessibility.js     # Lógica de acessibilidade e toggle
```

### CSS Implementado

**`accessibility.css`**
- Classes de utilitários (`.sr-only`, `.skip-link`)
- Tema de alto contraste completo
- Indicadores de foco aprimorados
- Suporte a preferências do sistema
- Transições suaves

**`accessibility.js`**
- Toggle de alto contraste
- Persistência de preferências
- Anúncios para leitores de tela
- Atalhos de teclado
- Skip links dinâmicos
- Validação semântica

---

## 🧪 Testes de Compatibilidade

### Navegadores Testados

| Navegador | Versão Mínima | Status |
|-----------|---------------|--------|
| Chrome | 90+ | ✅ Compatível |
| Firefox | 88+ | ✅ Compatível |
| Safari | 14+ | ✅ Compatível |
| Edge | 90+ | ✅ Compatível |

### Leitores de Tela Testados

| Leitor | Sistema | Status |
|--------|---------|--------|
| NVDA | Windows | ✅ Compatível |
| JAWS | Windows | ✅ Compatível |
| VoiceOver | macOS | ✅ Compatível |
| Narrator | Windows | ✅ Compatível |

### Dispositivos

- ✅ Desktop (1920x1080+)
- ✅ Tablet (768x1024)
- ✅ Mobile (375x667+)

---

## 📝 Boas Práticas para Manutenção

### Ao Adicionar Novos Elementos

1. **Use HTML semântico** - Escolha a tag correta (`<button>` para botões, `<nav>` para navegação)
2. **Adicione ARIA quando necessário** - Mas prefira HTML semântico quando possível
3. **Teste com teclado** - Navegue apenas com Tab/Enter
4. **Verifique contraste** - Use ferramentas como WAVE ou axe DevTools
5. **Teste com leitor de tela** - NVDA é gratuito para Windows

### Ao Criar Formulários

```html
<!-- BOM ✅ -->
<label for="name">Nome:</label>
<input id="name" type="text" required aria-required="true">

<!-- RUIM ❌ -->
<input type="text" placeholder="Nome">
```

### Ao Criar Botões

```html
<!-- BOM ✅ -->
<button aria-label="Fechar janela">X</button>

<!-- RUIM ❌ -->
<div onclick="close()">X</div>
```

---

## 🚀 Recursos Futuros (Planejados)

- [ ] Integração com Text-to-Speech (TTS)
- [ ] Tamanho de fonte ajustável
- [ ] Modo de leitura simplificada
- [ ] Suporte a comandos por voz

---

## 📞 Suporte e Feedback

Para reportar problemas de acessibilidade ou sugerir melhorias:
- Documente o problema detalhadamente
- Inclua navegador e leitor de tela (se aplicável)
- Descreva os passos para reproduzir

---

## ✅ Checklist de Acessibilidade

Ao revisar o código, verifique:

- [ ] Todas as imagens têm `alt` text descritivo
- [ ] Todos os inputs têm labels associados
- [ ] Elementos interativos são acessíveis por teclado
- [ ] Contraste de cores atende WCAG AA mínimo
- [ ] Estrutura HTML é semântica
- [ ] Erros são anunciados aos leitores de tela
- [ ] Foco é visível em todos os elementos
- [ ] Skip links funcionam corretamente
- [ ] Alto contraste funciona em todos os componentes

---

**Última atualização**: Novembro 2025  
**Versão**: 1.0.0  
**Conformidade**: WCAG 2.1 Nível AA
