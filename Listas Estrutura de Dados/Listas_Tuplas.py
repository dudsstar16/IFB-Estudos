##ESTRUTURA DE DADOS 

## LISTAS 

meusnumeros = [1 ,2, 3]
contatinhos = ["João", "Vitor", "Vitor", "Felipe"]
vazio = []

## usar indices para imprimir elementos da lista (0, 1, 2) começa sempre com 0 

print(contatinhos[2]) ## felipe 
print(contatinhos) # imprime todos os elementos 
print(contatinhos[3]) # undefined 

## obs: indices NEGATIVOS e tipos MISTURADOS 
print(meusnumeros, contatinhos)

mistura = [10, "texto", 3.14, True, meusnumeros]
print(mistura)
## apend() -- addiciona um elemento NO FINAL DA LISTA (USA MAIS)
contatinhos.append("Dante")
print(contatinhos)
## remove() -- remove a PRIMEIRA ocorrencia de um valor da lista
contatinhos.remove("vitor")
print(contatinhos)
## pop() -- remove e retorna um elemento pelo INDICE (remove o ultimo elemento da lista e retorna)
ultima = contatinhos.pop() # sem indice APAGA O ULTIMO ELEMENTO
print(ultima) # felipe
print(contatinhos) # joao, vitor
contatinhos.pop(0) # remove joao 
## insert() -- insere um elemento EM UMA POSIÇÃO ESPECIFICA 
contatinhos.insert(0, "luan")
print(contatinhos)
## sort() -- ORDEM ALFABETICA (USA MUITO) NÃO USA SE FOR MISTURADO 
contatinhos.sort()
print(contatinhos)
## reverse() -- INVERTE A ORDEM DOS ELEMENTOS SEM ordenar (USA MUITO)
contatinhos.reverse()
print(contatinhos)
## len() -- TAMANHO DA LISTA 
print(len(contatinhos)) 

for nome in contatinhos:
    print("Olá, ", contatinhos)



## TUPLAS QUE NÃO SE PODE ALTERAR (PODE TER TIPOS DIFERENTES)

minha_tupla = (1, 2, 3, 4) ## FAZER ASSIM

outra_tupla = 1, 2, 4, 5

tupla_unitaria = (10,)

cores = ("azul", "vermelho", "branco")

print(cores[0])
for cor in cores:
    print("Está é a cor para cada: ", cores)


"""VOCÊ NÃO QUER SABER MAIS DE MIM, IREI PULAR DO PÉ DE ALFACE :*( )"""

# Desempacotar tupla:

ponto = (3, 4)
x, y = ponto
print(x) # 3
print(y) # 4

# lista de tuplas
alunos = [("Ana", 8.5), ("Bruno", 7.0), ("Carla", 9.3)]

for nome, nota in alunos:
 print(f"{nome} tirou nota {nota}")

# ● Usar tuplas como chaves em dicionários:

coordenadas = {(0, 0): "origem", (1, 2): "ponto A"}

print(coordenadas[(1, 2)]) # ponto A SO USA COLCHETE NA IMPRESSAO

## exemplo com tres informações dentro de uma tupla 

produtos = [
 (1001, "Caneta", 1.50),
 (1002, "Caderno", 12.00),
 (1003, "Mochila", 75.90),
]
codigo_busca = 1002
for produto in produtos:
 codigo, nome, preco = produto
 if codigo == codigo_busca:
    print(f"Produto encontrado: {nome} - R$ {preco:.2f}")
    break
else:
 print("Produto não encontrado.")

## CONJUNTOS = ELEMENTOS UNICOS E NAO ORDENADOS 

## -- GARANTIR QUE NAO TENHA DUPLICATAS 
## pode adicionar e remover mas NÃO PODE ALTERAR UM ELEMENTO
## CHAVE

conjunto = {1, 2, 3}
conjunto.add(4)
conjunto.discard(2)
print(conjunto)

## OPERAÇÕES COM CONJUNTOS 

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("União:", A | B) # {1, 2, 3, 4, 5, 6}
print("Interseção:", A & B) # {3, 4}
print("Diferença A - B:", A - B) # {1, 2}
print("Diferença B - A:", B - A) # {5, 6}

# EXEMPLOO

curso_python = ["Ana", "Bruno", "Carla", "Daniel"]
curso_java = ["Bruno", "Elisa", "Carla", "Fernando"]
# Convertendo listas em conjuntos para operações de conjuntos (IMPORTANTE)
set_python = set(curso_python)
set_java = set(curso_java)
# Alunos que estão em ambos os cursos (interseção)
alunos_ambos = set_python & set_java
# Alunos que estão em pelo menos um dos cursos (união)
alunos_todos = set_python | set_java
# Alunos que estão apenas em Python (diferença)
apenas_python = set_python - set_java
# Alunos que estão apenas em Java (diferença)
apenas_java = set_java - set_python
print("Alunos em ambos os cursos:", alunos_ambos)
print("Alunos em pelo menos um dos cursos:", alunos_todos)
print("Alunos apenas no curso de Python:", apenas_python)
print("Alunos apenas no curso de Java:", apenas_java)


## DICIONARIOS 

# Criando um dicionário com chaves e valores

pessoa = {
 "nome": "Ana",
 "idade": 25,
 "cidade": "São Paulo"
}
print(pessoa)

print(pessoa["nome"]) # Ana
print(pessoa.get("idade")) # 25

## ADICIONAR E MODIFICAR 

pessoa["email"] = "ana@example.com" # adiciona novo par chave-valor
pessoa["idade"] = 26

## REMOVER ELEMENTOS 

del pessoa["cidade"] # remove a chave 'cidade'
email = pessoa.pop("email") # remove e retorna o valor associado a email

## recorrer um DIC 

for chave, valor in pessoa.items(): # pecorrer cada elemento dos valores, TEM QUE TER ITEMS para pecorrer
 print(f"{chave}: {valor}")

 ## IMPORTANTE : VAI USAR MAIS LISTA E DIC 

 ## EXEMPLO 

 contatos = {
 "Ana": "9999-1111",
 "Bruno": "8888-2222",
 "Carla": "7777-3333"
}
 
print("Lista de contatos:")

for nome, telefone in contatos.items():
 print(f"{nome}: {telefone}")

print()

nome_novo = "Daniel"
telefone_novo = "6666-4444"

if nome_novo in contatos: ## SO A CHAVE NAO PRECISA DE .ITEMS
 print(f"Contato {nome_novo} já existe. Atualizando telefone.")
else:
 print(f"Adicionando contato {nome_novo}.")
contatos[nome_novo] = telefone_novo


## FUNÇÕES EM PYTHON 

## organizar e evitar repetição 

def saudacao(nome):
  print(f"Olá, {nome}!")

saudacao("Maria")
saudacao("Joao")


## IMPORTAR OUTROS ARQUIVOS EM UM SO 

__name__ = '__main__'

if __name__ == '__main__':
  print_billing_doc()

## ARQUIVO PRINCIPAL 






