'''
Faça um programa que peça o tamanho de um arquivo para
download (em MB) e a velocidade de um link de Internet (em
Mbps), calcule e informe o tempo aproximado de download do
arquivo usando este link (em minutos).
'''

# peça o tamanho de um arquivo para download (em MB)

arquivo1 = float(input("\nInsira o Tamanho do arquivo para dowload em MB: "))

# e a velocidade de um link de Internet (em Mbps)

velocidade_link = float(input("Insira a Velocidade registrada em (Mbps): "))

# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

velocidade_mbps = velocidade_link / 8

tempo_segundos = arquivo1 / velocidade_mbps

temp_min = tempo_segundos / 60

print(f"\nO tempo aproximado de download do arquivo usando este link (em minutos) foi de {tempo_min} minutos.")

