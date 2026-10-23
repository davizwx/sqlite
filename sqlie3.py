import sqlite3

banco=sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

cursor.execute('CREATE TABLE peoas(nome text, idade integer, email text)')

cursor.execute('INSERT INTO pessoas VALUES ('davi', 15, 'davi.mandu@escola.pr.gov.br')')

banco.comit()               