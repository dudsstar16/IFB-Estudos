
-- CHAVES PRIMARIAS

CREATE TABLE endereco (
    id_endereco SERIAL PRIMARY KEY,
    descricao VARCHAR(400) NOT NULL,
    bairro VARCHAR(200) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(100) NOT NULL,
    cep CHAR(8) NOT NULL
);

CREATE TABLE bar (
    id_bar SERIAL PRIMARY KEY,
    nome VARCHAR(200) NOT NULL,
    id_endereco INTEGER REFERENCES endereco(id_endereco) NOT NULL
);

CREATE TABLE fabriante (
    id_fabricante SERIAL PRIMARY KEY,
    nome VARCHAR(200) NOT NULL,
    id_endereco INTEGER REFERENCES endereco(id_endereco) NOT NULL
);

CREATE TABLE cerveja (
    id_cerveja SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    id_fabricante INTEGER REFERENCES fabriante(id_fabricante) NOT NULL
);

CREATE TABLE frequentador (
    id_frequentador SERIAL PRIMARY KEY, 
    nome VARCHAR(200) NOT NULL,
    id_endereco INTEGER REFERENCES endereco(id_endereco) NOT NULL,
    id_cerveja INTEGER REFERENCES cerveja(id_cerveja) NOT NULL
);

CREATE TABLE telefone (
    id_telefone SERIAL PRIMARY KEY,
    numero CHAR(9) NOT NULL,
    dd CHAR(3) NOT NULL,
    id_frequentador INTEGER REFERENCES frequentador(id_frequentador) NOT NULL
);

-- CHAVES COMPOSTAS

CREATE TABLE servi (
    id_cerveja INTEGER REFERENCES cerveja(id_cerveja),
    id_bar INTEGER REFERENCES bar(id_bar),
    preco NUMERIC(6, 2) NOT NULL
    PRIMARY KEY (id_cerveja, id_bar)
);

CREATE TABLE frequenta (
    id_frequentador INTEGER REFERENCES frequentador(id_frequentador),
    id_bar INTEGER REFERENCES bar(id_bar),
    PRIMARY KEY (id_frequentador, id_bar)
);

CREATE TABLE aprecia (
    id_frequentador INTEGER REFERENCES frequentador(id_frequentador),
    id_cerveja INTEGER REFERENCES cerveja(id_cerveja),
    PRIMARY KEY (id_frequentador, id_cerveja)
);
