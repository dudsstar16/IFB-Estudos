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

        print("\n---Universo de Dragon Ball---")
        print("\n1. Cadastrar lutador")
        print("2. Listar lutadores")
        print("3. Simular ataque")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":

            try:
                print("\nTipos de lutadores: ")
                print("1 - Sayajin")
                print("2 - Androide")
                print("3 - Namekuseijin")

                raca = input("\nEscolha a raça: ")

                if not raca in ["1", "2", "3"]:
                    raise Exception ("\nTipo inválido. Por favor insira uma escolha válida.\n")
                    
                nome = input("Nome do lutador: ").strip()

                if not nome:
                    raise Exception("\nNome inválido. Tente novamente.\n")

                nivel = int(input("Nível de Poder: "))

                if nivel <= 0 or not nivel:
                    raise Exception("\nO nível precisa ser POSITIVO e não pode estar vazio. Tente novamente.\n")

                # Atribuir os dados a cada sublasse

                if raca == "1":
                    lutador = Saiyajin(nome, nivel)
                elif raca == "2":
                    lutador = Androide(nome, nivel)
                elif raca == "3":
                    lutador = Namekuseijin(nome, nivel)

                lutadores.append(lutador)

                print(f"\n{lutador.get_nome()} lutador cadastrado com sucesso.\n")

            except Exception as e:
                print(f"\nErro: {e}")  
            
        elif opcao == "2":

            if not lutadores:
                print("\nNenhum lutador cadastrado.\n")
            else:
                # Apresentar os indices por isso o enumerate 
                for i, lutador in enumerate(lutadores, start = 1):
                    print()
                    print(f"{i}. {lutador.get_nome()} - Poder: {lutador.get_nivel_poder()}")
            
        elif opcao == "3":

            if not lutadores:
                print("Nenhum lutador para atacar.\n")
            else:
                for i, lutador in enumerate(lutadores, start = 1):
                    print(f"\n{i}. {lutador.get_nome()}\n")

            try:    
                escolha = int(input("\nEscolha o número do lutador: "))
                if 1 <= escolha <= len(lutadores):
                    print(f"\n{lutadores[escolha - 1]}. {lutadores.get_nome()} vai atacar!\n")
                    # - 1 porque a lista começa no 0 (revisar, fiquei em dúvida)
                    lutadores[escolha - 1].atacar()

                else:
                    raise Exception ("\nNúmero inválido para escolha de lutador.\n")

            except Exception as e:
                print(f"\nErro: {e}\n")

        elif opcao == "0":
            print("\nEncerrando o Torneio. Até a próxima ! :D\n")
            break
        else:
            print("\nOpçao Inválida. Por favor, digite uma escolha válida.\n")


if __name__ == "__main__":
    main()
