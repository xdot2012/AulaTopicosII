# Descrição:
Código desenvolvido em conjunto durante as aulas de Tópicos II - [Aplicações Web], ministradas pelo professor Luis Henrique Silva Rodrigues, durante o semestre extraporâneo 2020/5, na Universidade Federal dos Vales do Jequitinhonha e Mucuri.
Estudamos o básico sobre aplicações do Framework Web para Python Django em sua versão 3.1.

# Configuração de Ambiente:
1. Clone ou faça o Download do projeto na sua máquina.
2. Dentro da pasta do projeto, crie o seu ambiente virtual:
<br>Caso não possua o virtualenv instalado:
```
pip install virtualenv
```
<br> Com o virtualenv instalado em sua máquina:
```
virtualenv env
```
3. Ative o ambiente virtual:
<br>Ao lado da pasta env: 
```
source env/bin/activate
```
4. Instale as dependências:
<br>Ao lado do arquivo requirements.txt, com o ambiente virtual ativado:
```
pip install -r requirements.txt
```
5. Efetue as migrações no banco de dados:
<br>Ao lado do arquivo manage.py, com o ambiente virtual ativado:
```
python manage.py migrate
```
6. Rode o Projeto:
<br>Ao lado do arquivo manage.py, com o ambiente virtual ativado: 
```
python manage.py runserver
```

# Mais Informações em:
<br>https://docs.djangoproject.com/pt-br/3.1/
