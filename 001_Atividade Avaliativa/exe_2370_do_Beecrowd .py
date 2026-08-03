## numero de alunos e time 

n, t = input().split()

n = int(n)
t = int(t)

lista = []

## entrada de nome e habilidade

for i in range(n):
    nome, habilidade = input().split()
    habilidade = int(habilidade) # converter para numero
    lista.append((nome, habilidade)) ## incluir na lista
    
## ordenar a habilidade do maior para o menor 

lista.sort(key=lambda aluno: aluno[1], reverse=True)

## criar a quantidade de listas para cada time 

times = []

for i in range(t):
    times.append([])
    
## atribuir de forma alternada cada aluno para cada time
    
for i in range(n): # pecorrer pela quantidade de aluno 
    indice_time = i % t # utilizar o indice em modulo de t
    times[indice_time].append(lista[i])
    
## imprimir

for i in range(t):
    
    # printa Time (indice, a partir do 1)
    print(f"Time {i + 1}")
    
    times[i].sort(key=lambda aluno: aluno[0])
    
    # printa os nomes dos alunos
    for aluno in times[i]:
        print(aluno[0])
    
    print()