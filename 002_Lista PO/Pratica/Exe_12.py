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

class Lutador(ABC):

    @abstractmethod
    def get_nome(self):
            pass 
        self.nivel_poder = nivel_poder
        self.ataque = ataque 

# SUBCLASSES

'''

Em seguida, implemente subclasses como Saiyajin,
Androide e Namekuseijin, cada uma com um comportamento
específico   ao   atacar.  

'''

class Saiyajin(Lutador):
    def __init__(self, nome, nivel_poder, ataque):
        super().__init__(nome, nivel_poder, ataque)

class Androide(Lutador):
    def __init__(self, nome, nivel_poder, ataque):
        super().__init__(nome, nivel_poder, ataque)

class Namekuseijin(Lutador):
    def __init__(self, nome, nivel_poder, ataque):
        super().__init__(nome, nivel_poder, ataque)

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

    while True:

        print("\n---Universo de Dragon Ball---\n")
        print("\n1. ")



if __name__ == "__main__":
    main()