
-------------------------------

ate o slide 62 (12/08)

-------------------------------

-------------------------------

ate o slide 84 (17/08) - finalizado

-------------------------------

Autor Importante (livros de BD): Carlos A.Heuser

# Modelo Conceitual e DER

> Etapa de aprendizagem: **Teoria — Modelagem de Dados**

## Objetivo

Compreender como representar, de forma visual e independente de tecnologia, as informações e regras de um negócio antes de criar tabelas no banco de dados.

---

## 1. O que é o modelo conceitual?

O **modelo conceitual** é a visão mais geral do banco de dados. Ele descreve **quais informações existem no negócio** e **como elas se relacionam**, sem se preocupar com SQL, tipos de dados ou com o SGBD que será usado.

Ele é usado para conversar com usuários, clientes e áreas de negócio, validando se o sistema representa a realidade corretamente.

### Exemplo

Em uma loja, existem clientes, produtos e pedidos. Um cliente realiza pedidos, e um pedido contém produtos.

Neste momento, ainda não definimos nomes de tabelas nem comandos SQL: apenas entendemos o negócio.

---

## 2. DER — Diagrama Entidade-Relacionamento

O **DER** é a representação gráfica do modelo conceitual. Ele mostra principalmente:

- **Entidades:** coisas importantes sobre as quais queremos armazenar dados.
- **Atributos:** características das entidades.
- **Relacionamentos:** associações entre entidades.
- **Cardinalidades:** quantas ocorrências podem participar de um relacionamento.

---

## 3. Entidade

Uma **entidade** é algo do mundo real que precisa ser identificado e sobre o qual desejamos guardar informações.

Exemplos:

- Cliente
- Produto
- Pedido
- Funcionário
- Curso
- Aluno

No DER, a entidade costuma ser representada por um **retângulo**.

> Dica: normalmente entidades são substantivos. Pergunte: “Sobre quais coisas preciso armazenar dados?”

---

## 4. Atributo

Um **atributo** é uma característica que descreve uma entidade.

| Entidade | Exemplos de atributos |
| --- | --- |
| Cliente | CPF, nome, e-mail, telefone |
| Produto | código, nome, preço, estoque |
| Pedido | número, data, valor total |

No DER clássico, atributos são representados por **elipses** ligadas à entidade.

### Tipos importantes de atributo

- **Simples:** não pode ser dividido de forma útil. Ex.: CPF.
- **Composto:** pode ser separado em partes. Ex.: endereço → rua, número, cidade e CEP.
- **Multivalorado:** pode ter mais de um valor. Ex.: telefones de um cliente.
- **Derivado:** é calculado a partir de outro dado. Ex.: idade, calculada pela data de nascimento.
- **Identificador:** distingue cada ocorrência da entidade. Ex.: CPF do cliente ou código do produto.

---

## 5. Relacionamento

Um **relacionamento** indica como entidades se associam.

Exemplos:

- Cliente **realiza** Pedido.
- Pedido **contém** Produto.
- Aluno **cursa** Disciplina.
- Funcionário **trabalha em** Departamento.

No DER, o relacionamento costuma ser representado por um **losango**.

> Dica: relacionamentos normalmente usam verbos. Pergunte: “O que uma entidade faz ou tem em relação à outra?”

---

## 6. Cardinalidade — conceito essencial

A **cardinalidade** define a quantidade de ocorrências de uma entidade que podem se relacionar com outra.

| Cardinalidade | Significado | Exemplo |
| --- | --- | --- |
| **1:1** | Uma ocorrência se relaciona com, no máximo, uma ocorrência da outra entidade. | Pessoa possui um CPF. |
| **1:N** | Uma ocorrência se relaciona com muitas ocorrências da outra entidade. | Um cliente realiza vários pedidos. |
| **N:N** | Muitas ocorrências se relacionam com muitas ocorrências. | Alunos cursam várias disciplinas; disciplinas possuem vários alunos. |

### Leitura de exemplo

`Cliente 1:N Pedido` significa:

- Um cliente pode realizar vários pedidos.
- Um pedido pertence a um único cliente.

---

## 7. Participação: obrigatória ou opcional

Além da quantidade, é necessário definir se a participação no relacionamento é obrigatória.

| Notação | Significado |
| --- | --- |
| `0..1` | Zero ou uma ocorrência: opcional. |
| `1..1` | Exatamente uma ocorrência: obrigatório. |
| `0..N` | Zero ou muitas ocorrências: opcional. |
| `1..N` | Uma ou muitas ocorrências: obrigatório. |

Exemplo: um cliente pode ainda não ter feito pedidos (`0..N`), mas todo pedido deve pertencer a um cliente (`1..1`).

---

## 8. Entidade forte e entidade fraca

### Entidade forte

Possui identificador próprio e pode existir independentemente.

**Exemplo:** `Cliente`, identificado por CPF ou `id_cliente`.

### Entidade fraca

Depende de outra entidade para ser identificada ou para existir.

**Exemplo:** `ItemPedido` depende de `Pedido`; sozinho, ele não tem sentido no sistema.

---

## 9. Como transformar o modelo conceitual em modelo lógico

O modelo conceitual não cria diretamente o banco, mas orienta a criação das tabelas.

| No modelo conceitual | No modelo lógico/relacional |
| --- | --- |
| Entidade | Tabela |
| Atributo | Coluna |
| Identificador | Chave primária (PK) |
| Relacionamento 1:N | Chave estrangeira (FK) no lado N |
| Relacionamento N:N | Nova tabela associativa com FKs |

### Exemplo: relacionamento 1:N

No DER:

```text
Cliente 1 ── realiza ── N Pedido
```

No banco relacional:

```text
Cliente(id_cliente, nome, cpf)
Pedido(id_pedido, data, id_cliente)
```

`id_cliente` em `Pedido` é uma chave estrangeira que aponta para `Cliente`.

### Exemplo: relacionamento N:N

No DER:

```text
Aluno N ── cursa ── N Disciplina
```

No banco relacional, cria-se uma tabela associativa:

```text
Aluno(id_aluno, nome)
Disciplina(id_disciplina, nome)
Matricula(id_aluno, id_disciplina, data_matricula)
```

---

## 10. Passo a passo para criar um DER

1. Entenda o problema e as regras do negócio.
2. Liste os substantivos importantes: candidatos a entidades.
3. Liste as características de cada entidade: atributos.
4. Defina um identificador para cada entidade.
5. Descubra as associações entre entidades: relacionamentos.
6. Defina cardinalidade e obrigatoriedade.
7. Valide o diagrama com exemplos reais do negócio.

---

## O que é mais importante para estudos e mercado

Priorize dominar:

1. Diferença entre modelo **conceitual**, **lógico** e **físico**.
2. Identificação correta de **entidades**, **atributos** e **relacionamentos**.
3. Cardinalidades **1:1**, **1:N** e **N:N**.
4. Participação obrigatória e opcional (`0..1`, `1..1`, `0..N`, `1..N`).
5. Transformação do DER em tabelas, PKs e FKs.
6. Relacionamentos N:N e a criação de uma tabela associativa.
7. Leitura e levantamento de regras de negócio antes de modelar.

> No trabalho, uma modelagem bem feita evita dados duplicados, relacionamentos incorretos e retrabalho no desenvolvimento.

---

## Revisão rápida

> O modelo conceitual mostra a realidade do negócio. No DER, entidades representam coisas, atributos descrevem essas coisas, relacionamentos mostram associações e cardinalidades informam quantas ocorrências participam de cada associação.

---

## Checklist de aprendizagem

- [ ] Sei explicar o objetivo do modelo conceitual.
- [ ] Consigo identificar entidades e atributos em um enunciado.
- [ ] Sei criar relacionamentos com verbos.
- [ ] Entendo as cardinalidades 1:1, 1:N e N:N.
- [ ] Sei identificar participação obrigatória e opcional.
- [ ] Sei transformar um relacionamento 1:N em chave estrangeira.
- [ ] Sei resolver um relacionamento N:N com uma tabela associativa.
