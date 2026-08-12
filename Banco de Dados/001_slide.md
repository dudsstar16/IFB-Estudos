
------------------

slide (1) ate a pagina 26 (/08)

------------------

------------------

slide (1) ate a pagina 58 (10/08)

------------------

------------------

slide (1) finalizado (12/08)

------------------


# Banco de Dados — Conceitos Fundamentais

> Etapa de aprendizagem: **Teoria**

## Objetivo

Entender o que é um banco de dados, como ele é administrado e quais conceitos são essenciais para estudos e para o mercado de trabalho.

---

## 1. Banco de Dados (BD)

Um **banco de dados** é uma coleção organizada de dados relacionados, criada para atender a um propósito específico.

- Os dados são **persistentes**: permanecem armazenados até serem removidos explicitamente.
- Pode ser visto como um arquivo eletrônico de uma empresa.
- Exemplos: clientes, produtos, vendas, funcionários e estoque.

---

## 2. SGBD

**SGBD** significa **Sistema Gerenciador de Banco de Dados**. É o software que permite criar, consultar, alterar, proteger e administrar bancos de dados.

Exemplos: PostgreSQL, MySQL, SQL Server, Oracle e MongoDB.

### Funções principais

- Definir tabelas, campos e regras dos dados.
- Inserir, consultar, atualizar e excluir dados.
- Controlar usuários e permissões.
- Garantir integridade, segurança e recuperação após falhas.
- Permitir acesso simultâneo de vários usuários.

---

## 3. Bancos operacionais e analíticos

| Tipo | Objetivo | Exemplo |
| --- | --- | --- |
| **Operacional (OLTP)** | Registrar operações diárias, com rapidez e consistência. | Registrar uma venda ou pagamento. |
| **Analítico (OLAP)** | Analisar muitos dados e apoiar decisões. | Dashboard de vendas anual. |

### OLTP

- Muitas operações pequenas: vendas, pedidos, estoque e pagamentos.
- Geralmente usa SQL e bancos relacionais.
- Precisa de consistência e segurança.

### OLAP

- Usado para relatórios, indicadores e dashboards.
- Trabalha com dados históricos e grandes volumes.
- É comum utilizar modelos desnormalizados e esquemas dimensionais.

---

## 4. Modelos de Banco de Dados

### Modelo relacional — o mais importante

Organiza os dados em **tabelas relacionadas** e normalmente é consultado com SQL.

- **Chave primária (PK):** identifica unicamente cada registro. Ex.: `id_cliente`.
- **Chave estrangeira (FK):** conecta uma tabela a outra. Ex.: `pedido.id_cliente`.
- Possui alta integridade: as regras ajudam a evitar dados inconsistentes.

Exemplo de tabelas: `Cliente`, `Pedido` e `Produto`.

### Modelo objeto-relacional

Combina o modelo relacional com recursos de orientação a objetos, permitindo tipos de dados mais complexos. PostgreSQL é um exemplo conhecido.

### NoSQL

É usado quando o problema exige alta escala, estrutura flexível ou tipos específicos de relacionamento.

| Tipo | Uso típico | Exemplo |
| --- | --- | --- |
| Documento | Dados em JSON e estrutura flexível. | MongoDB |
| Chave-valor | Acesso muito rápido por chave. | Redis |
| Colunar | Grandes volumes de dados. | Cassandra |
| Grafo | Relacionamentos complexos. | Neo4j |

> NoSQL não substitui automaticamente SQL: a escolha depende da necessidade do sistema.

---

## 5. Níveis de modelagem

1. **Conceitual:** visão do negócio, geralmente com Diagrama Entidade-Relacionamento (DER).
   - Exemplo: um cliente realiza um pedido.
2. **Lógico:** tabelas, atributos, chaves e relacionamentos.
   - Exemplo: `Cliente(id, nome)` e `Pedido(id, id_cliente, data)`.
3. **Físico:** implementação no SGBD.
   - Inclui tipos de dados, índices, armazenamento e comandos SQL.

---

## 6. Profissionais da área

| Profissional | Responsabilidade |
| --- | --- |
| DBA | Mantém o banco seguro, rápido, disponível e com backup. |
| Administrador de Dados | Cuida de políticas, qualidade e governança. |
| Modelador de Dados | Cria os modelos conceitual, lógico e físico. |
| Desenvolvedor | Usa SQL e integra o banco aos sistemas. |
| Analista de Dados/BI | Consulta dados e cria relatórios para decisões. |

---

## 7. Prioridade para o mercado de trabalho

Estude nesta ordem:

1. **SQL:** `SELECT`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`, `INSERT`, `UPDATE` e `DELETE`.
2. **Modelagem relacional:** tabelas, PK, FK, relacionamentos e cardinalidade.
3. **Integridade e normalização:** reduzir redundância e evitar dados inválidos.
4. **Transações:** garantir operações corretas e completas.
5. **Índices e desempenho:** entender por que uma consulta pode ficar lenta.
6. **Segurança, backup e recuperação.**
7. **PostgreSQL ou MySQL:** escolha um para praticar.
8. **NoSQL básico:** saiba quando MongoDB, Redis ou bancos de grafo são adequados.

---

## Revisão rápida

> O banco de dados guarda informações; o SGBD administra essas informações; o modelo relacional organiza dados em tabelas; e SQL permite consultar e alterar os dados.

**Foco inicial recomendado:** SQL + modelagem de dados + PostgreSQL/MySQL + integridade + segurança básica.

---

## Checklist

- [ ] Sei diferenciar BD e SGBD.
- [ ] Entendo o que são dados persistentes.
- [ ] Sei diferenciar OLTP e OLAP.
- [ ] Entendo PK, FK e relacionamentos.
- [ ] Sei diferenciar modelos conceitual, lógico e físico.
- [ ] Entendo quando SQL e NoSQL são usados.
- [ ] Consigo escrever consultas SQL básicas.
