-- ESTUDO DE CASO 3 - DETRAN
-- Cinco linhas em cada tabela.

-- 1. Cinco modelos.
INSERT INTO modelo (codigo_modelo, nome) VALUES
(100001, 'Gol 1.6'),
(100002, 'Onix LT'),
(100003, 'CG 160'),
(100004, 'Corolla XEI'),
(100005, 'HB20 Comfort');

-- 2. Cinco categorias.
INSERT INTO categoria (codigo_categoria, nome) VALUES
(10, 'Automovel'),
(20, 'Motocicleta'),
(30, 'Caminhao'),
(40, 'Onibus'),
(50, 'Utilitario');

-- 3. Cinco proprietarios.
INSERT INTO proprietario
(cpf, nome, sexo, data_nascimento, idade, bairro, cidade, estado)
VALUES
('11111111111', 'Maria Oliveira', 'F', '1988-03-15', 38, 'Asa Norte', 'Brasilia', 'DF'),
('22222222222', 'Marcos Silva', 'M', '1985-07-20', 41, 'Taguatinga', 'Brasilia', 'DF'),
('33333333333', 'Ana Souza', 'F', '1993-11-10', 32, 'Aguas Claras', 'Brasilia', 'DF'),
('44444444444', 'Beatriz Costa', 'F', '1990-05-08', 36, 'Ceilandia', 'Brasilia', 'DF'),
('55555555555', 'Miguel Santos', 'M', '1995-01-25', 31, 'Guara', 'Brasilia', 'DF');

-- 4. Cinco telefones.
INSERT INTO tel_proprietario (cpf, telefone) VALUES
('11111111111', '61999990001'),
('22222222222', '61999990002'),
('33333333333', '61999990003'),
('44444444444', '61999990004'),
('55555555555', '61999990005');

-- 5. Cinco locais.
INSERT INTO local
(codigo_local, posicao_geografica, velocidade_permitida)
VALUES
(1, 'Eixao Norte - Brasilia', 60),
(2, 'Avenida Comercial - Taguatinga', 40),
(3, 'BR-060 - Goiania', 80),
(4, 'Avenida Afonso Pena - Belo Horizonte', 50),
(5, 'Avenida Paulista - Sao Paulo', 30);

-- 6. Cinco tipos de infracao.
INSERT INTO tipo_infracao (codigo_tipo, descricao, valor) VALUES
(101, 'Excesso de velocidade', 195.23),
(102, 'Avanco de sinal vermelho', 293.47),
(103, 'Parada sobre faixa de pedestres', 130.16),
(104, 'Uso de celular ao volante', 293.47),
(105, 'Estacionamento em local proibido', 130.16);

-- 7. Cinco radares.
INSERT INTO radar (id_radar, nome, uf) VALUES
(1, 'Radar Eixao Norte', 'DF'),
(2, 'Radar Avenida Comercial', 'DF'),
(3, 'Radar BR-060', 'GO'),
(4, 'Radar Avenida Afonso Pena', 'MG'),
(5, 'Radar Avenida Paulista', 'SP');

-- 8. Cinco agentes de transito.
INSERT INTO agente_de_transito
(matricula, nome, data_contratacao, tempo_de_servico)
VALUES
('A001', 'Carlos Mendes', '2018-02-01', '8 anos'),
('A002', 'Fernanda Lima', '2020-06-10', '6 anos'),
('A003', 'Joao Pereira', '2019-04-15', '7 anos'),
('A004', 'Luciana Alves', '2021-08-20', '5 anos'),
('A005', 'Ricardo Gomes', '2017-01-12', '9 anos');

-- 9. Cinco veiculos.
-- Maria possui dois veiculos.
INSERT INTO veiculo
(placa, chassi, cor_predominante, ano_fabricacao,
 codigo_modelo, codigo_categoria, cpf)
VALUES
('JKL1A23', '9BWZZZ377VT000001', 'Prata', 2020, 100001, 10, '11111111111'),
('ABC1D23', '9BGKS48U0LG000002', 'Branco', 2021, 100002, 10, '11111111111'),
('DEF4G56', '9BGKS48U0LG000003', 'Preto', 2019, 100002, 10, '22222222222'),
('GHI7J89', '9C2KC1670LR000004', 'Vermelho', 2022, 100003, 20, '33333333333'),
('MNO2K34', '9BHBG51CAKP000005', 'Azul', 2023, 100005, 10, '55555555555');

-- 10. Cinco infracoes.
INSERT INTO infracao
(data_hora, placa, codigo_tipo, velocidade, uf,
 codigo_local, id_radar, matricula)
VALUES
('2026-09-01 08:30:00', 'JKL1A23', 101, 78, 'DF', 1, 1, NULL),
('2026-09-02 10:15:00', 'JKL1A23', 102, NULL, 'DF', 2, NULL, 'A001'),
('2026-09-03 14:20:00', 'ABC1D23', 101, 55, 'DF', 2, 2, NULL),
('2026-09-04 09:10:00', 'DEF4G56', 103, NULL, 'GO', 3, NULL, 'A002'),
('2026-09-05 17:45:00', 'GHI7J89', 104, 60, 'DF', 1, 1, NULL);
