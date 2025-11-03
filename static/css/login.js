document.addEventListener('DOMContentLoaded', function() {
 
    const btnLogin = document.getElementById('btnFazerLogin');
    const form = document.getElementById('loginForm');

    if (btnLogin && form) {
        btnLogin.addEventListener('click', function(e) {
            
            // Apenas submete o formulário do Django
            form.submit();
        });
    }

    // 2. LÓGICA DO TOGGLE DE SENHA
    const passwordInput = document.getElementById('id_password');
    const toggle = document.getElementById('togglePasswordLogin'); 
    
    if (passwordInput && toggle) {
        toggle.addEventListener('click', function() {
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);
            this.textContent = (type === 'password') ? '👁️' : '🔒'; 
        });
    }
});