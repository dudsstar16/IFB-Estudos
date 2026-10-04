-- =====================================================
-- CONSULTA 1
-- Proprietarios que possuem mais de um veiculo.
-- =====================================================

SELECT
    p.nome AS proprietario,
    COUNT(v.placa) AS quantidade_veiculos
FROM proprietario p
JOIN veiculo v ON p.cpf = v.cpf
GROUP BY p.cpf, p.nome
HAVING COUNT(v.placa) > 1;


-- =====================================================
-- CONSULTA 2
-- Proprietarios cujo nome comeca com a letra M.
-- =====================================================

SELECT
    p.nome AS proprietario,
    p.cpf,
    v.placa
FROM proprietario p
JOIN veiculo v ON p.cpf = v.cpf
WHERE p.nome LIKE 'M%'
ORDER BY p.nome, v.placa;


-- =====================================================
-- CONSULTA 3
-- Valor total das ocorrencias de cada tipo de infracao.
-- =====================================================

SELECT
    t.descricao AS tipo_infracao,
    SUM(t.valor) AS valor_total
FROM tipo_infracao t
JOIN infracao i ON t.codigo_tipo = i.codigo_tipo
GROUP BY t.codigo_tipo, t.descricao
ORDER BY t.descricao;


-- =====================================================
-- CONSULTA 4
-- Infracoes em que a velocidade foi maior que a permitida.
-- =====================================================

SELECT
    i.placa,
    i.velocidade AS velocidade_aferida,
    l.velocidade_permitida,
    l.posicao_geografica AS local_infracao
FROM infracao i
JOIN local l ON i.codigo_local = l.codigo_local
WHERE i.velocidade > l.velocidade_permitida
ORDER BY i.placa;


-- =====================================================
-- CONSULTA 5
-- Infracoes ocorridas no Distrito Federal.
-- =====================================================

SELECT
    i.placa,
    p.nome AS proprietario,
    t.descricao AS tipo_infracao,
    i.data_hora,
    i.uf
FROM infracao i
JOIN veiculo v ON i.placa = v.placa
JOIN proprietario p ON v.cpf = p.cpf
JOIN tipo_infracao t ON i.codigo_tipo = t.codigo_tipo
WHERE i.uf = 'DF'
ORDER BY i.data_hora;
