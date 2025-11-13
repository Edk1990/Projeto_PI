// Função para verificar se o usuário está autenticado
function isAuthenticated() {
    const token = localStorage.getItem('auth_token');
    return token !== null;
}

// Função para proteger rotas
function protectRoute() {
    if (!isAuthenticated()) {
        window.location.href = 'tela_login_admin.html';
    }
}

// Função para fazer logout
function logout() {
    localStorage.removeItem('auth_token');
    window.location.href = 'tela_login_admin.html';
}

// Função para criar token de autenticação
function createAuthToken() {
    const timestamp = Date.now();
    const random = Math.random().toString(36).substring(2);
    return `${timestamp}-${random}`;
}

// Função para verificar força da senha
function validatePassword(password) {
    const minLength = 8;
    const hasNumber = /[0-9]/.test(password);
    const hasUpper = /[A-Z]/.test(password);
    const hasLower = /[a-z]/.test(password);
    
    if (password.length < minLength) {
        return 'A senha deve ter pelo menos 8 caracteres';
    }
    
    if (!hasNumber) {
        return 'A senha deve conter pelo menos um número';
    }
    
    if (!hasUpper || !hasLower) {
        return 'A senha deve conter letras maiúsculas e minúsculas';
    }
    
    return null;
}
