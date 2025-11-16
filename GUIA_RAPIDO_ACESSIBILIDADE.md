# 🚀 Guia Rápido - Recursos de Acessibilidade

## Para Usuários

### 🎨 Como Ativar o Modo Alto Contraste

#### Opção 1: Botão na Tela
1. Procure o botão **"Alto Contraste"** no canto superior direito
2. Clique no botão
3. A página mudará para cores de alto contraste
4. Para desativar, clique novamente no botão (agora mostrando "Modo Normal")

#### Opção 2: Atalho de Teclado
- Pressione **Alt + C** em qualquer momento
- Funciona em todas as páginas do sistema

### 📢 Usando com Leitores de Tela

O sistema funciona automaticamente com:
- **NVDA** (Windows - gratuito)
- **JAWS** (Windows)
- **VoiceOver** (Mac/iOS)
- **Narrator** (Windows)

**Dicas:**
- Todas as informações importantes são anunciadas
- Use as teclas de navegação do seu leitor de tela normalmente
- Os formulários têm instruções claras
- Erros são anunciados automaticamente

### ⌨️ Navegação por Teclado

- **Tab**: Avançar para o próximo elemento
- **Shift + Tab**: Voltar para elemento anterior
- **Enter**: Clicar em links e botões
- **Espaço**: Marcar checkboxes e radio buttons
- **Setas**: Navegar em listas suspensas

### ⏩ Pular para Conteúdo Principal

1. Pressione **Tab** assim que a página carregar
2. O primeiro link será "Pular para conteúdo principal"
3. Pressione **Enter** para ir direto ao conteúdo
4. Economiza tempo evitando menus de navegação

---

## Para Desenvolvedores

### 📁 Arquivos Criados

```
Projeto_PI/
├── assets/
│   ├── css/
│   │   └── accessibility.css        # Estilos de acessibilidade
│   └── js/
│       └── accessibility.js         # Funcionalidades de acessibilidade
├── ACESSIBILIDADE.md                # Documentação completa
└── GUIA_RAPIDO_ACESSIBILIDADE.md   # Este arquivo
```

### 🔧 Como Funciona

#### CSS (`accessibility.css`)
- Tema de alto contraste com classe `.high-contrast` no `<body>`
- Contraste 21:1 (WCAG AAA)
- Estilos para skip links
- Indicadores de foco aprimorados

#### JavaScript (`accessibility.js`)
- Módulo auto-executável (IIFE)
- Cria botão de toggle automaticamente
- Salva preferência no localStorage
- Sistema de anúncios para leitores de tela
- Atalhos de teclado (Alt+C)

### 🎯 Como Usar nos Seus Arquivos

#### 1. Adicione os links no `<head>`

```html
<link rel="stylesheet" href="assets/css/accessibility.css">
```

#### 2. Adicione o script antes do `</body>`

```html
<script src="assets/js/accessibility.js"></script>
```

#### 3. Pronto! Funciona automaticamente

O botão de toggle aparecerá sozinho e todas as funcionalidades estarão ativas.

### 📝 Modificações Feitas em Cada Página

#### ✅ tela__login.html (Página Inicial)
- HTML semântico (`<main>`, `<nav>`, `<aside>`)
- Meta description
- Atributos ARIA
- Links de acessibilidade

#### ✅ tela_perguntas.html (Formulário)
- Labels para todos os inputs
- Fieldsets e legends para grupos
- ARIA attributes completos
- Progress bar acessível
- Mensagens de erro anunciadas

#### ✅ tela_login_admin.html
- Formulário acessível
- Mensagens de erro com `role="alert"`
- Autocomplete para campos
- Anúncios de sucesso/erro

#### ✅ dashboard_admin.html
- Tabela semântica com roles ARIA
- Cabeçalhos ordenáveis acessíveis
- Estatísticas com live regions
- Filtros com labels corretos
- Paginação acessível

#### ✅ tela_agradecimento_.html
- Anúncio automático de sucesso
- HTML semântico
- Links de acessibilidade

### 🧪 Como Testar

#### Teste de Alto Contraste
1. Abra qualquer página
2. Pressione Alt + C
3. Verifique se as cores mudaram
4. Recarregue a página - deve manter o modo ativado

#### Teste com Teclado
1. Use apenas Tab, Shift+Tab, Enter, Espaço
2. Verifique se todos os elementos são acessíveis
3. Observe indicadores de foco visíveis

#### Teste com Leitor de Tela
1. Baixe NVDA (gratuito): https://www.nvaccess.org/
2. Inicie o NVDA
3. Navegue pelo site usando teclas de navegação
4. Verifique se todas as informações são anunciadas

### 🐛 Debug

#### Ver Anúncios do Leitor de Tela
No console do navegador:
```javascript
// Testar anúncio manualmente
AccessibilityModule.announceToScreenReader("Teste de anúncio");
```

#### Verificar Estado do Alto Contraste
No console:
```javascript
// Ver se alto contraste está ativo
document.body.classList.contains('high-contrast')

// Ver preferência salva
localStorage.getItem('high-contrast-mode')
```

#### Forçar Estado
```javascript
// Ativar
document.body.classList.add('high-contrast');

// Desativar
document.body.classList.remove('high-contrast');
```

### 📊 Conformidade

#### ✅ WCAG 2.1 Nível AA
- Contraste de cores adequado
- Navegação por teclado completa
- Labels em todos os formulários
- Mensagens de erro claras
- Foco visível

#### ✅ WAI-ARIA 1.2
- Roles apropriados
- States e properties corretos
- Live regions implementadas
- Labels e descriptions

---

## 🆘 Solução de Problemas

### Botão de Alto Contraste não Aparece
1. Verifique se `accessibility.js` está sendo carregado
2. Abra o Console (F12) e procure por erros
3. Verifique o caminho do arquivo

### Alto Contraste não Salva
1. Verifique se o navegador permite localStorage
2. Teste em modo anônimo/privado (pode bloquear storage)

### Leitor de Tela não Funciona
1. Certifique-se que o leitor está instalado e ativo
2. Teste com NVDA (gratuito) primeiro
3. Verifique se as páginas têm os atributos ARIA

---

## 📚 Recursos Adicionais

### Ferramentas de Teste
- **WAVE**: https://wave.webaim.org/
- **axe DevTools**: Extensão do Chrome
- **Lighthouse**: Auditoria no Chrome DevTools

### Aprender Mais
- **WCAG Guidelines**: https://www.w3.org/WAI/WCAG21/quickref/
- **MDN ARIA**: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA
- **WebAIM**: https://webaim.org/

---

**Dúvidas?** Consulte o arquivo `ACESSIBILIDADE.md` para documentação completa.
