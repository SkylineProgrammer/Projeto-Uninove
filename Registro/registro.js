//Script Comunicação
const API_CADASTRO_URL = 'http://localhost:8000/api/cadastro/';

document.getElementById('botaoCriarConta').addEventListener('click', enviarCadastro);

function enviarCadastro(event) {
    event.preventDefault(); 

    const username = document.getElementById('usuario').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value; 

    const dadosCadastro = {
        username: username,
        email: email,
        password: password
    };

    fetch(API_CADASTRO_URL, {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(dadosCadastro) 
    })
    .then(response => {
        if (response.status === 201) {
            alert('✅ Conta criada com sucesso! Você pode logar agora.');
          
            return;
        } else if (response.status === 400) {
            return response.json().then(data => {
                alert(`❌ Erro no cadastro: ${JSON.stringify(data)}`);
            });
        } else {
            alert('⚠️ Erro no servidor. Tente novamente mais tarde.');
        }
    })
    .catch(error => {
        console.error('Erro de conexão:', error);
        alert('🚨 Falha ao conectar. Seu servidor desligado!');
    });
}
