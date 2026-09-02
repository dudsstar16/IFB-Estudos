
CREATE TABLE categoria (
	id_categoria SERIAL PRIMARY KEY,
	nome VARCHAR(200) NOT NULL,
	descricao VARCHAR(500) 
);

CREATE TABLE veiculos(
	placa CHAR(8) PRIMARY KEY,
	chassi VARCHAR(18) NOT NULL,
	ano INTEGER NOT NULL,
	cor VARCHAR(100) NOT NULL,
	id_categoria INTEGER REFERENCES categoria(id_categoria)
);
