'''
 Crie um programa em Python que recebe um valor em reais e
o converte para outra moeda. Use um menu para escolher a
moeda de destino:
1. Dólar
2. Euro
3. Libra
4. Iene
O programa deve perguntar o valor em reais e exibir o valor
convertido para a moeda escolhida. Use valores fictícios para
as taxas de conversão:
1 Real = 0.19 Dólar
1 Real = 0.17 Euro
1 Real = 0.15 Libra
1 Real = 25 Ienes
'''

# recebe um valor em reais e o converte para outra moeda

moeda_de_destino = int(input("Insira um valor em reais: "))

lista = [Dólar, Euro, Libra, Iene]

for i, moeda_de_destino in enumerate(lista, start=1):
    print(f"{i}: {moeda_de_destino}").lower()

print(f"A escolhida foi a {moeda_de_destino}")

if moeda_de_destino = 1:










