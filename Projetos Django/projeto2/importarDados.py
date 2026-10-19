
from cadpessoas.models import Pessoas  # modelo/tabela Pessoas do app cadpessoas
import csv

# Abre o CSV e itera por cada linha (cada linha vira um dict)
with open('cadastro_pessoas.csv', newline='', encoding='utf-8') as csvfile:
    arquivo = csv.DictReader(csvfile)

    for linha in arquivo:
        # Cria um registro Pessoas com os campos do CSV
        Pessoas.objects.create(
            nome=linha['nome'],
            email=linha['email'],
            telefone=linha['telefone'],
            cidade=linha['cidade']
        )

print("Importação concluída com sucesso!")
