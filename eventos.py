import sqlite3
conexao = sqlite3.connect('sqlm2s2.dados02')
sql = '''CREATE TABLE eventos (
	id INTEGER NOT NULL,
	titulo TEXT,
	"data" TEXT,
	"local" TEXT,
	organizador_id INTEGER NOT NULL,
	CONSTRAINT eventos_PK PRIMARY KEY (id),
	CONSTRAINT eventos_FK FOREIGN KEY (organizador_id) REFERENCES organizador(id)
);
'''
cursor.execute(sql)
conexao.commit()
conexao.close()