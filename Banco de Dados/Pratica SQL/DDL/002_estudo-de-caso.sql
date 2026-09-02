
CREATE TABLE copa (
	ano SERIAL PRIMARY KEY,
	data_inicio DATE NOT NULL,
	data_fim DATE NOT NULL,
	cidade_abertura VARCHAR(200) NOT NULL,
	cidade_fim VARCHAR(200) NOT NULL
);

CREATE TABLE pais (
	id_pais SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	sigla VARCHAR(4) NOT NULL
); 

CREATE TABLE pessoa (
	id_pessoa SERIAL PRIMARY KEY,
	nome VARCHAR(200) NOT NULL,
	data_nascimento DATE NOT NULL,
	id_pais INTEGER REFERENCES pais(id_pais) NOT NULL
);

CREATE TABLE equipe (
	id_equipe SERIAL PRIMARY KEY,
	nome VARCHAR(200) NOT NULL,
	id_pais INTEGER REFERENCES pais(id_pais) NOT NULL,
	treinador INTEGER REFERENCES pessoa(id_pessoa) NOT NULL
);

// CHAVES COMPOSTAS

CREATE TABLE sede (
    ano INTEGER REFERENCES copa(ano),
    id_pais INTEGER REFERENCES pais(id_pais),
    PRIMARY KEY (ano, id_pais)
);

CREATE TABLE jogo (
	numero SERIAL,
	ano INTEGER REFERENCES copa(ano), 
	data_jogo DATE NOT NULL,
	hora TIME NOT NULL,
	estadio VARCHAR(200) NOT NULL,
	equipe1 INTEGER REFERENCES equipe(id_equipe) NOT NULL,
	equipe2 INTEGER REFERENCES equipe(id_equipe) NOT NULL,
	gols_equipe1 INTEGER NOT NULL,
	gols_equipe2 INTEGER NOT NULL,
	PRIMARY KEY (numero, ano)
);

CREATE TABLE jogadores (
    id_pessoa INTEGER REFERENCES pessoa(id_pessoa),
    id_equipe INTEGER REFERENCES equipe(id_equipe),
    PRIMARY KEY (id_pessoa, id_equipe)
);
