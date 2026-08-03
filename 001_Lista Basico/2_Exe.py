#ler o custo de fábrica de um carro 

custo_fabrica_carro = float(input("Insira o valor referente ao custo de fábrica de um carro: "))

'''
O custo ao consumidor de um carro novo é a soma do custo
de fábrica com a porcentagem do distribuidor e dos impostos
(aplicados ao custo de fábrica). Supondo que a porcentagem
do distribuidor seja de 12% do preço de fábrica e os impostos
de 30% do preço de fábrica
'''

p_distribuidor = custo_fabrica_carro * 0.12
imposto = custo_fabrica_carro * 0.30

preco_final = custo_fabrica_carro + p_distribuidor + imposto

#imprimir o custo ao consumidor (final)

print(f"\nO custo ao consumidor é equivalente a {preco_final}")

print("\nDados Analiticos Abaixo")
print(f"\nA Porcentagem do Distribuidor: {p_distribuidor}")
print(f"\nValor do Imposto Aplicado: {imposto}")
print(f"\nO calculo realizado foi a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica)")