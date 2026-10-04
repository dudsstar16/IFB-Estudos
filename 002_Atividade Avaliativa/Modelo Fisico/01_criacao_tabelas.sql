-- ESTUDO DE CASO 3 - DETRAN
-- Criacao das tabelas conforme o modelo logico.

-- Tabela dos modelos dos veiculos.
CREATE TABLE modelo (
    codigo_modelo INTEGER PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

-- Tabela das categorias dos veiculos.
CREATE TABLE categoria (
    codigo_categoria INTEGER PRIMARY KEY,
    nome VARCHAR(30) NOT NULL
);

-- Tabela dos proprietarios.
CREATE TABLE proprietario (
    cpf VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sexo CHAR(1) NOT NULL,
    data_nascimento DATE NOT NULL,
    idade INTEGER NOT NULL,
    bairro VARCHAR(50) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    estado CHAR(2) NOT NULL
);

-- Um proprietario pode possuir mais de um telefone.
CREATE TABLE tel_proprietario (
    cpf VARCHAR(11) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
    PRIMARY KEY (cpf, telefone),
    FOREIGN KEY (cpf) REFERENCES proprietario(cpf)
);

-- Tabela dos locais onde podem ocorrer infracoes.
CREATE TABLE local (
    codigo_local INTEGER PRIMARY KEY,
    posicao_geografica VARCHAR(100) NOT NULL,
    velocidade_permitida INTEGER NOT NULL
);

-- Tabela dos tipos de infracao e seus valores.
CREATE TABLE tipo_infracao (
    codigo_tipo INTEGER PRIMARY KEY,
    descricao VARCHAR(100) NOT NULL,
    valor DECIMAL(10,2) NOT NULL
);

-- Tabela dos radares.
CREATE TABLE radar (
    id_radar INTEGER PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    uf VARCHAR(2) NOT NULL
);

-- Tabela dos agentes de transito.
CREATE TABLE agente_de_transito (
    matricula VARCHAR(20) PRIMARY KEY,
    nome VARCHAR(200) NOT NULL,
    data_contratacao DATE NOT NULL,
    tempo_de_servico VARCHAR(30) NOT NULL
);

-- Tabela dos veiculos.
-- O veiculo e ligado ao modelo, a categoria e ao proprietario.
CREATE TABLE veiculo (
    placa CHAR(7) PRIMARY KEY,
    chassi VARCHAR(17) NOT NULL,
    cor_predominante VARCHAR(20) NOT NULL,
    ano_fabricacao INTEGER NOT NULL,
    codigo_modelo INTEGER NOT NULL,
    codigo_categoria INTEGER NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    FOREIGN KEY (codigo_modelo) REFERENCES modelo(codigo_modelo),
    FOREIGN KEY (codigo_categoria) REFERENCES categoria(codigo_categoria),
    FOREIGN KEY (cpf) REFERENCES proprietario(cpf)
);

-- Tabela das infracoes.
-- A chave primaria usa data/hora, placa e tipo da infracao.
CREATE TABLE infracao (
    data_hora TIMESTAMP NOT NULL,
    placa CHAR(7) NOT NULL,
    codigo_tipo INTEGER NOT NULL,
    velocidade INTEGER,
    uf CHAR(2) NOT NULL,
    codigo_local INTEGER NOT NULL,
    id_radar INTEGER,
    matricula VARCHAR(20),
    PRIMARY KEY (data_hora, placa, codigo_tipo),
    FOREIGN KEY (placa) REFERENCES veiculo(placa),
    FOREIGN KEY (codigo_tipo) REFERENCES tipo_infracao(codigo_tipo),
    FOREIGN KEY (codigo_local) REFERENCES local(codigo_local),
    FOREIGN KEY (id_radar) REFERENCES radar(id_radar),
    FOREIGN KEY (matricula) REFERENCES agente_de_transito(matricula)
);
