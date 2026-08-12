# Banco de Dados — Conceitos Fundamentais

> Etapa de aprendizagem: **Teoria**

## Objetivo desta etapa

Compreender o que é um banco de dados, como ele é administrado e quais conceitos são mais cobrados em estudos e mais úteis no mercado de trabalho.

---

## 1. O que é um Banco de Dados?

Um **Banco de Dados (BD)** é uma coleção organizada de dados relacionados, armazenados para um objetivo específico.

Os dados são **persistentes**: continuam guardados mesmo após o sistema ser fechado e só são removidos por uma ação explícita.

Exemplos de dados que uma empresa pode guardar:

- Clientes
- Produtos
- Vendas e pedidos
- Funcionários
- Estoque

### Exemplo simples

Em uma loja virtual, o banco de dados guarda o cadastro do cliente, os produtos disponíveis e os pedidos realizados.

---

## 2. O que é um SGBD?

**SGBD** significa **Sistema Gerenciador de Banco de Dados**. É o software usado para criar, consultar, alterar, proteger e administrar um banco de dados.

Exemplos comuns:

- PostgreSQL
- MySQL
- SQL Server
- Oracle Database
- MongoDB

### Funções de um SGBD

- Definir a estrutura dos dados (tabelas, campos e regras).
- Inserir, consultar, alterar e excluir dados.
- Controlar usuários e permissões.
- Evitar inconsistências e duplicações indevidas.
- Fazer backup e recuperar dados após falhas.
- Permitir acesso simultâneo de vários usuários.

---

## 3. Por que usar Banco de Dados?

| Benefício | Em termos simples |
| --- | --- |
| Organização | Os dados ficam estruturados e fáceis de localizar. |
| Segurança | Cada pessoa acessa apenas o que tem permissão. |
| Integridade | Regras ajudam a manter os dados corretos. |
| Menos redundância | Evita repetir a mesma informação várias vezes. |
| Recuperação | Backups ajudam a restaurar dados perdidos. |
| Desempenho | Consultas e acessos podem ser otimizados. |

---

## 4. Bancos Operacionais e Analíticos

### Operacional (OLTP)

Usado nas operações do dia a dia.

- Registra vendas, pedidos, pagamentos e atualizações de estoque.
- Realiza muitas operações pequenas e rápidas.
- Precisa de alta consistência e segurança.
- Normalmente utiliza bancos relacionais e SQL.

**Exemplo:** registrar uma compra em um e-commerce.

### Analítico (OLAP)

Usado para analisar dados e apoiar decisões.

- Gera relatórios, dashboards e indicadores.
- Consulta grandes quantidades de dados, geralmente históricos.
- É comum usar dados desnormalizados e esquemas dimensionais.

**Exemplo:** descobrir qual produto gerou mais vendas no último ano.

---

## 5. Modelos de Banco de Dados

### Modelo relacional — prioridade máxima

Organiza informações em **tabelas relacionadas**. É o modelo mais comum em sistemas empresariais.

Exemplo:

- Tabela `Cliente`
- Tabela `Pedido`
- Tabela `Produto`

As tabelas se conectam por chaves:

- **Chave primária (PK):** identifica de forma única cada registro. Ex.: `id_cliente`.
- **Chave estrangeira (FK):** cria a ligação com outra tabela. Ex.: `pedido.id_cliente`.

### Modelo objeto-relacional

Combina o modelo relacional com recursos inspirados em orientação a objetos, permitindo trabalhar melhor com tipos de dados mais complexos. O PostgreSQL é um exemplo conhecido.

### NoSQL

Usado quando os dados são muito flexíveis, há grande escala ou o problema exige um formato diferente de tabelas relacionais.

| Tipo | Uso típico | Exemplo |
| --- | --- | --- |
| Documento | Dados em JSON, com estrutura flexível | MongoDB |
| Chave-valor | Acesso muito rápido por chave | Redis |
| Colunar | Análises de grandes volumes de dados | Cassandra |
| Grafo | Relações complexas entre informações | Neo4j |

> NoSQL não substitui automaticamente SQL. A melhor opção depende do problema a ser resolvido.

---

## 6. Níveis de Modelagem de Dados

### Modelo conceitual

Mostra a visão do negócio, sem detalhes técnicos. Normalmente usa Diagrama Entidade-Relacionamento (DER).

**Exemplo:** um cliente realiza um pedido.

### Modelo lógico

Transforma a visão do negócio em tabelas, atributos, chaves e relacionamentos.

**Exemplo:** `Cliente(id, nome)` e `Pedido(id, id_cliente, data)`.

### Modelo físico

Mostra como o banco será implementado no SGBD.

Inclui tipos de dados, índices, comandos SQL, armazenamento e decisões de desempenho.

---

## 7. Profissionais da área

| Profissional | Responsabilidade principal |
| --- | --- |
| DBA | Mantém o banco funcionando, seguro, rápido e com backup. |
| Administrador de Dados | Define políticas, qualidade e governança dos dados. |
| Modelador de Dados | Cria modelos conceituais, lógicos e físicos. |
| Desenvolvedor | Usa SQL e integra o banco aos sistemas. |
| Analista de Dados/BI | Consulta e analisa dados para gerar relatórios e decisões. |

---

## 8. O que é essencial para o mercado de trabalho?

Priorize estes assuntos nesta ordem:

1. **SQL:** `SELECT`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`, `INSERT`, `UPDATE` e `DELETE`.
2. **Modelagem relacional:** tabelas, PK, FK, relacionamentos e cardinalidade.
3. **Integridade dos dados:** regras para evitar dados inválidos ou inconsistentes.
4. **Normalização:** organização das tabelas para reduzir redundância.
5. **Transações:** garantir que operações críticas sejam concluídas corretamente.
6. **Índices e desempenho:** saber por que uma consulta pode ficar lenta.
7. **Segurança, backup e recuperação.**
8. **Um SGBD relacional:** pratique principalmente PostgreSQL ou MySQL.
9. **NoSQL básico:** entenda quando MongoDB, Redis ou grafos fazem sentido.

---

## 9. Resumo para revisão rápida

> O banco de dados guarda informações; o SGBD administra essas informações; o modelo relacional organiza os dados em tabelas; e SQL permite consultar e alterar os dados.

Para iniciar bem na área, foque em:

**SQL + modelagem de dados + PostgreSQL/MySQL + integridade + segurança básica.**

---

## Checklist de aprendizagem

- [ ] Sei explicar a diferença entre BD e SGBD.
- [ ] Entendo o que são dados persistentes.
- [ ] Sei diferenciar OLTP de OLAP.
- [ ] Entendo PK, FK e relacionamento entre tabelas.
- [ ] Sei a diferença entre modelo conceitual, lógico e físico.
- [ ] Entendo quando SQL e NoSQL podem ser usados.
- [ ] Consigo escrever consultas SQL básicas.
