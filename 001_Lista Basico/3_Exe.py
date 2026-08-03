'''
Faça um programa em Python que leia dois números inteiros
quaisquer para as variáveis A e B, efetue a troca dos valores
de forma que A passe a armazenar o valor de B e que B
passe armazenar o valor de A e que imprima os valores
trocados
'''

a = int(input("\nDigite o Primeiro Número Inteiro: "))
b = int(input("\nDigite o Primeiro Número Inteiro: "))

print(f"\nA variavel A é {a}")
print(f"\nA variavel B é {b}")

a, b = b, a

print(f"\nA troca dos valores destaca a variavel A como {a}")

print(f"\nSendo assim tendo variavel B como {b}")