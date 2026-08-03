# solicita o nome do aluno

aluno = input("Insira o Nome do Aluno: ")

# solicita as notas de uma disciplina e o peso delas

n1 = float(input("Digite a Primeira nota: "))
p1 = int(input("O peso da nota 1: "))                  
n2 = float(input("Digite a Segunda nota: "))
p2 = int(input("O peso da nota 2: "))
n3 = float(input("Digite a Terceira nota: "))
p3 = int(input("O peso da nota 3: "))

media = (n1*p1) + (n2*p2) + (n3*p3) / p1 + p2 + p3

if media >= 7:
    print(f"O aluno {aluno} foi Aprovado :D")
elif media < 7:
    print(f"O aluno {aluno} está de recuperação :(" + "\nVoce consegue !!!")
else:
    print(f"O aluno {aluno} foi Reprovado :o" + "\nEstude mais !!!")




