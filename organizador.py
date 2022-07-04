import sqlite3 
conexao = sqlite3.connect('sqlm2s2.dados02')
sql = ''' CREATE TABLE organizador (
	id INTEGER NOT NULL,
	nome TEXT,
	email TEXT,
	cpf TEXT,
	CONSTRAINT organizador_PK PRIMARY KEY (id)
);
'''
cursor.execute(sql)
conexao.commit()
conexao.clore()