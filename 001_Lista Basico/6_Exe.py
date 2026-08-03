'''
 Faça um programa em Python que leia a temperatura em
graus Celsius e determine a classificação da temperatura:
 • Menor que 0°C: Frio extremo
 • De 0°C a 10°C: Frio
 • De 11°C a 25°C: Ameno
 • De 26°C a 35°C: Quente
 • Maior que 35°C: Muito quente
''' 

# leia a temperatura em graus Celsius

temp_c = float(input("\nInsira a temperatura registrada: "))


'''
 • Menor que 0°C: Frio extremo
 • De 0°C a 10°C: Frio
 • De 11°C a 25°C: Ameno
 • De 26°C a 35°C: Quente
 • Maior que 35°C: Muito quente
'''

if temp_c < 0:
    print("Frio extremo")
elif temp_c >= 0 and temp_c <= 10:
    print("Frio")
elif temp_c >= 11 and temp_c <= 25:
    print("Ameno")
elif temp_c >= 26 and temp_c <= 35:
    print("Quente")
else:
    print("Muito quente")