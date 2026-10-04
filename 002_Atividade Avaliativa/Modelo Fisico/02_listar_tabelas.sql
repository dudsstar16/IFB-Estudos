-- Mostra as tabelas criadas no banco detran_atividade.

SELECT table_name AS tabela_criada
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;
