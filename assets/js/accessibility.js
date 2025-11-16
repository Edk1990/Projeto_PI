/**
 * =============================================================
 * MÓDULO DE ACESSIBILIDADE
 * - Toggle de Alto Contraste
 * - Persistência de Preferências
 * - Notificações de Acessibilidade
 * =============================================================
 */

(function() {
    'use strict';

    // Constantes
    const STORAGE_KEY = 'high-contrast-mode';
    const HIGH_CONTRAST_CLASS = 'high-contrast';
    const NOTIFICATION_DURATION = 3000;

    /**
     * Inicializa o módulo de acessibilidade
     */
    function init() {
        createAccessibilityToggle();
        loadUserPreference();
        setupKeyboardShortcuts();
        announcePageLoad();
    }

    /**
     * Cria o botão de toggle de alto contraste
     */
    function createAccessibilityToggle() {
        const toggle = document.createElement('button');
        toggle.className = 'accessibility-toggle';
        toggle.setAttribute('aria-label', 'Alternar modo de alto contraste');
        toggle.setAttribute('aria-pressed', 'false');
        toggle.setAttribute('title', 'Clique para ativar/desativar alto contraste (Atalho: Alt+C)');
        
        const text = document.createElement('span');
        text.textContent = 'Alto Contraste';
        toggle.appendChild(text);
        
        toggle.addEventListener('click', toggleHighContrast);
        document.body.appendChild(toggle);
    }

    /**
     * Alterna o modo de alto contraste
     */
    function toggleHighContrast() {
        const body = document.body;
        const isHighContrast = body.classList.toggle(HIGH_CONTRAST_CLASS);
        
        // Atualizar estado do botão
        const toggle = document.querySelector('.accessibility-toggle');
        if (toggle) {
            toggle.setAttribute('aria-pressed', isHighContrast);
            const text = toggle.querySelector('span');
            if (text) {
                text.textContent = isHighContrast ? 'Modo Normal' : 'Alto Contraste';
            }
        }
        
        // Salvar preferência
        saveUserPreference(isHighContrast);
        
        // Mostrar notificação
        showNotification(
            isHighContrast ? 
            'Modo de Alto Contraste Ativado' : 
            'Modo Normal Ativado'
        );
        
        // Anunciar mudança para leitores de tela
        announceToScreenReader(
            isHighContrast ? 
            'Alto contraste ativado. A página agora está em modo de alto contraste.' : 
            'Alto contraste desativado. A página voltou ao modo normal.'
        );
    }

    /**
     * Salva preferência do usuário no localStorage
     */
    function saveUserPreference(isHighContrast) {
        try {
            localStorage.setItem(STORAGE_KEY, isHighContrast ? 'true' : 'false');
        } catch (e) {
            console.warn('Não foi possível salvar preferência de acessibilidade:', e);
        }
    }

    /**
     * Carrega preferência do usuário
     */
    function loadUserPreference() {
        try {
            const savedPreference = localStorage.getItem(STORAGE_KEY);
            if (savedPreference === 'true') {
                document.body.classList.add(HIGH_CONTRAST_CLASS);
                const toggle = document.querySelector('.accessibility-toggle');
                if (toggle) {
                    toggle.setAttribute('aria-pressed', 'true');
                    const text = toggle.querySelector('span');
                    if (text) {
                        text.textContent = 'Modo Normal';
                    }
                }
            }
        } catch (e) {
            console.warn('Não foi possível carregar preferência de acessibilidade:', e);
        }
    }

    /**
     * Configura atalhos de teclado
     */
    function setupKeyboardShortcuts() {
        document.addEventListener('keydown', function(e) {
            // Alt + C = Toggle Alto Contraste
            if (e.altKey && e.key.toLowerCase() === 'c') {
                e.preventDefault();
                toggleHighContrast();
            }
            
            // Alt + 1 = Ir para conteúdo principal
            if (e.altKey && e.key === '1') {
                e.preventDefault();
                const main = document.querySelector('main') || document.querySelector('[role="main"]');
                if (main) {
                    main.focus();
                    main.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }
        });
    }

    /**
     * Mostra notificação temporária
     */
    function showNotification(message) {
        // Remove notificação anterior se existir
        const existingNotification = document.querySelector('.accessibility-notification');
        if (existingNotification) {
            existingNotification.remove();
        }
        
        const notification = document.createElement('div');
        notification.className = 'accessibility-notification';
        notification.setAttribute('role', 'status');
        notification.setAttribute('aria-live', 'polite');
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        // Remove notificação após alguns segundos
        setTimeout(() => {
            notification.style.opacity = '0';
            setTimeout(() => notification.remove(), 300);
        }, NOTIFICATION_DURATION);
    }

    /**
     * Anuncia mensagem para leitores de tela
     */
    function announceToScreenReader(message) {
        const announcement = document.createElement('div');
        announcement.className = 'sr-only';
        announcement.setAttribute('role', 'status');
        announcement.setAttribute('aria-live', 'polite');
        announcement.setAttribute('aria-atomic', 'true');
        announcement.textContent = message;
        
        document.body.appendChild(announcement);
        
        // Remove após 1 segundo
        setTimeout(() => announcement.remove(), 1000);
    }

    /**
     * Anuncia carregamento da página para leitores de tela
     */
    function announcePageLoad() {
        const pageTitle = document.title;
        setTimeout(() => {
            announceToScreenReader(`Página carregada: ${pageTitle}`);
        }, 500);
    }

    /**
     * Adiciona skip links para navegação rápida
     */
    function createSkipLinks() {
        const skipLink = document.createElement('a');
        skipLink.href = '#main-content';
        skipLink.className = 'skip-link';
        skipLink.textContent = 'Pular para o conteúdo principal';
        skipLink.setAttribute('aria-label', 'Pular para o conteúdo principal');
        
        document.body.insertBefore(skipLink, document.body.firstChild);
        
        // Adicionar id ao conteúdo principal se não existir
        const main = document.querySelector('main') || 
                     document.querySelector('.form-area') || 
                     document.querySelector('.dashboard-content') ||
                     document.querySelector('.welcome-container');
        
        if (main && !main.id) {
            main.id = 'main-content';
            main.setAttribute('tabindex', '-1');
        }
    }

    /**
     * Melhora foco em elementos interativos
     */
    function enhanceFocusManagement() {
        // Adicionar indicador visual de foco em elementos importantes
        const interactiveElements = document.querySelectorAll('a, button, input, select, textarea');
        
        interactiveElements.forEach(element => {
            if (!element.hasAttribute('tabindex')) {
                // Mantém ordem natural de tabulação
                element.setAttribute('tabindex', '0');
            }
        });
    }

    /**
     * Valida e melhora semântica HTML existente
     */
    function validateAndEnhanceSemantics() {
        // Adicionar role em formulários sem role
        const forms = document.querySelectorAll('form:not([role])');
        forms.forEach(form => {
            form.setAttribute('role', 'form');
        });
        
        // Adicionar aria-label em inputs sem label
        const inputs = document.querySelectorAll('input:not([aria-label]):not([aria-labelledby])');
        inputs.forEach(input => {
            const placeholder = input.getAttribute('placeholder');
            const name = input.getAttribute('name');
            if (placeholder) {
                input.setAttribute('aria-label', placeholder);
            } else if (name) {
                input.setAttribute('aria-label', name);
            }
        });
    }

    /**
     * Detecta preferência do sistema operacional
     */
    function detectSystemPreferences() {
        // Detectar preferência de alto contraste do sistema
        if (window.matchMedia && window.matchMedia('(prefers-contrast: high)').matches) {
            console.info('Sistema operacional está em modo de alto contraste');
        }
        
        // Detectar preferência de movimento reduzido
        if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
            console.info('Sistema operacional prefere movimento reduzido');
            document.documentElement.style.setProperty('--animation-duration', '0.01ms');
        }
    }

    // Inicializar quando o DOM estiver pronto
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            init();
            createSkipLinks();
            enhanceFocusManagement();
            validateAndEnhanceSemantics();
            detectSystemPreferences();
        });
    } else {
        // DOM já está pronto
        init();
        createSkipLinks();
        enhanceFocusManagement();
        validateAndEnhanceSemantics();
        detectSystemPreferences();
    }

    // Expor função global para uso em páginas específicas se necessário
    window.AccessibilityModule = {
        toggleHighContrast: toggleHighContrast,
        announceToScreenReader: announceToScreenReader,
        showNotification: showNotification
    };

})();
