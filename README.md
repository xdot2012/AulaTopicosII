# Configuração de Ambiente:
1. Clone ou faça o Download do projeto na sua máquina.
2. Dentro da pasta do projeto, crie o seu ambiente virtual:
  pip install virtualenv (Caso não possua o virtualenv instalado)
  virtualenv env
3. Ative o ambiente virtual:
  (Ao lado da pasta env) source env/bin/activate
4. Instale as dependências:
  (Ao lado do arquivo requirements.txt, com o ambiente virtual ativado) pip install -r requirements.txt
5.Efetue as migrações no banco de dados:
  (Ao lado do arquivo manage.py, com o ambiente virtual ativado) python manage.py migrate
6. Rode o Projeto:
  (Ao lado do arquivo manage.py, com o ambiente virtual ativado) python manage.py runserver

# Mais Informações em:
https://docs.djangoproject.com/pt-br/3.1/
