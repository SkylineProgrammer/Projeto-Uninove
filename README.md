# Cria o ambiente virtual chamado "venv" ( necessário pro projeto funcionar, segue comandos abaixo de explicação)
python -m venv venv

# Ativa o ambiente virtual
.\venv\Scripts\Activate

# Para atualizar o pip ( é opcional mas e sempre bom deixar atualizado)
python -m pip install --upgrade pip

# Ja instala os requisitos com base no arquivo de requirimentos pra funcionar o projeto
pip install -r requirements.txt

<img width="793" height="120" alt="image" src="https://github.com/user-attachments/assets/f41abb1d-7229-4ea9-90ca-c0678b25b58e" />

# cria os arquivos no banco local
python manage.py migrate

# Para rodar o servidor local  ( http://127.0.0.1:8000/) só copiar e colar no navegador 
python manage.py runserver

# "Antes de testar por gentileza entre nesses 3 links e apertem em Get após executarem o comando runserver acima" para que sejam gerados perguntas randômicas pela IA Gemini para cada dificuldade, só e necessário fazer isso uma vez, após isso basta usar o comando runserver para quando quiser adentrar a aplicação"
http://127.0.0.1:8000/api/quiz/gerar/F/

http://127.0.0.1:8000/api/quiz/gerar/M/

http://127.0.0.1:8000/api/quiz/gerar/D/
<img width="1207" height="379" alt="image" src="https://github.com/user-attachments/assets/a8e9234b-0620-48a0-96c5-50138ea32729" />

# Demais duvidas estamos a disposição "Equipe Bit a bit"
 
