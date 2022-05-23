# frameworksfullstack

Atividade contínua 01

FAÇA UMA PROGRAMA WEB UTILIZANDO PYTHON E FLASK
QUE RECEBA DOIS NUMEROS INTEIROS E UMA OPERACAO
MATEMATICA (SOMA, SUBTRACAO, DIVISAO E MULTIPLICACAO)
 E RETORNE O VALOR CALCULADO INDICADO NA OPERACAO
A ENTREGA DEVE SER FEITA NO GITHUB

Atividade contínua 02

Faça uma aplicacao web em Flask que armazene dados de um cadastro de alunos com nome, email e endereco do aluno. A aplicacao deve listar os dados gravados.
A entrega deve ser preferencialmente em github e com prints comprovando a execucao da aplicacao.
A aplicacao pode gravar dados em postgres, mysql, sqllite ou mssql server.

Atividade contínua 03

Desenvolva um microservico utilizando Docker, em python e Flask, que armazene dados de um cadastro de um produto com os campos nome,  categoria e preco.
A aplicacao deve listar os dados gravados.
A entrega deve ser preferencialmente em github e com prints comprovando a execucao da aplicacao.
A aplicacao pode gravar dados em postgres ou mysql.
Utilize como referencia o projeto https://github.com/antoniodiasabc/docker_postgres

Atividade contínua 04

Este projeto usa sqlalchemy com postgresql
https://github.com/antoniodiasabc/docker_postgres
Execute ele com docker e tire um print da tabela posts com dados
(o proprio projeto tem um passo a passo para execucao)
Este projeto usa sqlalchemy com mysql
https://github.com/antoniodiasabc/sqlalchemy
Execute ele com docker (na parte de banco de dados mysql) tire um print das tabelas project e project_manager  com os dados armazenados
(o proprio projeto tem um passo a passo para execucao)


Alunos: 
Hires Serva de Maria Menezes - 1904889 / 
Rodrigo Augusto Alves - 1904668

docker_postgres
##para ajustar o ip do banco de dados

docker-compose up

docker network inspect bridge

ver o ip do container do banco de dados postgres
parar o container, ajustar o ip em config.py e subir de novo

para criar a tabea deste schema
docker-compose run web /usr/local/bin/python create_db.py

acessar localhost:5050 e inserir dados

para confirmar que funcionou
docker ps

obter o id do container
docker exec -it fae98c9e4b78 /bin/bash

su postgres

psql -U sis_web

select * from posts;

para obter a secret key
Run that code in a python shell:

import os

os.urandom(24)

b'\x1d\xc6\x0f[\xed\x18\xd6:5\xe0\x0f\rG\xaf\xb4\xf4HT\xef\xc1\xf1\xa89f'

nao esquecer de remover a letra b no comeco da string

pip install psycopg2-binary

testar localmente antes de subir o container
python3.8 app.py
