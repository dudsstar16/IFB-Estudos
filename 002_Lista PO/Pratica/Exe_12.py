'''

No universo de Dragon Ball, desenvolva um sistema em
Python para simular um torneio de artes marciais, utilizando
orientação a objetos. 

Crie uma classe totalmente abstrata
chamada Lutador, contendo apenas métodos abstratos para
obter o nome do lutador,  o  nível de poder e  realizar  um
ataque.  

'''
from abc import ABC, abstractmethod

# TOTALMENTE ABSTRATA 
#  - Perceba que ela não possui atributos.
# - Ela apenas obriga as subclasses.


class Lutador(ABC):

    @abstractmethod
    def get_nome(self):
            pass 

    @abstractmethod
    def get_nivel_poder(self):
        pass

    @abstractmethod
    def atacar(self):
        pass

# SUBCLASSES

'''

Em seguida, implemente subclasses como Saiyajin,
Androide e Namekuseijin, cada uma com um comportamento
específico   ao   atacar.  

'''

class Saiyajin(Lutador):
    def __init__(self, nome, nivel_poder):
        self.nome = nome
        self.nivel_poder = nivel_poder

# Subclasses devem acessar seus próprios atributos
#   - logo não se usa o SUPER

    def get_nome(self):
        return self.nome

    def get_nivel_poder(self):
        return self.nivel_poder

# POLIMORFISMO 
#   - cada subclasse possui um ataque diferente

    def atacar(self):
        print(f"{self.nome} lançou um Kamehameha!")

class Androide(Lutador):
    def __init__(self, nome, nivel_poder):
        self.nome = nome
        self.nivel_poder = nivel_poder

# Subclasses devem acessar seus próprios atributos
#   - logo não se usa o SUPER

    def get_nome(self):
        return self.nome

    def get_nivel_poder(self):
        return self.nivel_poder

# POLIMORFISMO 
#   - cada subclasse possui um ataque diferente

    def atacar(self):
        print(f"{self.nome} disparou um Canhão de Energia!")

class Namekuseijin(Lutador):
    def __init__(self, nome, nivel_poder):
        self.nome = nome
        self.nivel_poder = nivel_poder

# Subclasses devem acessar seus próprios atributos
#   - logo não se usa o SUPER

    def get_nome(self):
        return self.nome

    def get_nivel_poder(self):
        return self.nivel_poder

# POLIMORFISMO 
#   - cada subclasse possui um ataque diferente

    def atacar(self):
        print(f"{self.nome} utilizou o Makankosappo!")

# MENU 

'''

O   sistema   deve   conter   um   menu
interativo que permita cadastrar lutadores de diferentes raças,
listar   todos   os   lutadores   inscritos   no   torneio   e   simular
ataques, demonstrando o uso de herança, abstração total e
polimorfismo. 

Implemente também tratamento de exceções,
garantindo que os nomes não estejam vazios e que o nível de
poder   seja   um   valor   numérico   positivo.

'''

def main():

    lutadores = []

    while True:

        print("\n---Universo de Dragon Ball---\n")
        print("\n1. Cadastrar lutador")
        print("2. Listar lutadores")
        print("3. Simular ataque")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            try:
                print("\n1 - Sayajin")
                print("\n2 - Androide")
                print("\n3 - Namekuseijin\n")

                raca = input("\nEscolha a raça: ")
                nome = input("Nome do lutador: ")

                if not nome.strip():
                    raise ValueError("\nNome inválido. Tente novamente.")

                nivel = int(input("Nível de Poder: "))

                if nivel <= 0:
                    raise ValueError("\nO nível precisa ser POSITIVO. Tente novamente.")

                if raca == "1":
                    lutador = Saiyajin(nome, nivel)
                elif raca == "2":
                    lutador = Androide(nome, nivel)
                else:
                    lutador = Namekuseijin(nome, nivel)

                lutadores.append(lutador)

            except ValueError as e:
                print(f"Erro: {e}")  
            
        elif opcao == "2":
            for lutador in lutadores:
                print()
                print(f"{lutador.get_nome()} - Poder: {lutador.get_nivel_poder()}")
            
        elif opcao == "3":
            for lutador in lutadores:
                lutador.atacar()

        elif opcao == "0":
            print("\nObrigada por utilizar os nossos Serviços. Volte sempre. :D")
            break
        else:
            print("\nOpçao Inválida. Por favor, digite uma escolha válida.")


if __name__ == "__main__":
    main()