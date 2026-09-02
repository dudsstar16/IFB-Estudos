
INSERT INTO categoria (id_categoria, nome, descricao)
VALUES 
	(1, 'Esportivo', 'a'),
	(2, 'Passeio', 'b'),
	(3, 'Utilitário', 'j'),
	(4, 'Carga', 's'),
	(5, 'Transporte', 'i');

INSERT INTO veiculos (placa, chassi, ano, cor, id_categoria)
VALUES 
	('888888NY', 'GFDBNKMLASWINJK365', 2022, 'Branco', 2),
	('777777LA', 'GFDBNKMLA9WINJKA12', 2014, 'Cinza', 1),
	('6F5GG475', 'SFDBNKMLASWINJK458', 2001, 'Preto', 5),
	('GH12H6BR', 'JFDBNKMLASWINJK456', 2003, 'Branco', 3),
	('FG7856AL', 'AFDBNKMLASWINJKA11', 2010, 'Azul', 4);

UPDATE veiculos SET ano = 2024 WHERE placa = '6F5GG475';

UPDATE veiculos SET cor = 'Laranja' WHERE placa = '888888NY';

UPDATE categoria SET nome = 'Caminhão' WHERE nome = 'Carga';
UPDATE categoria SET descricao = 'Carros utilizados para passeio' WHERE nome = 'Passeio';

DELETE FROM veiculos WHERE cor = 'Azul';
