'''
Desenvolva um sistema para gerenciar veículos de transporte
público em uma cidade inteligente. Crie uma classe abstrata
VeiculoTransporte,   com   os   atributos   placa   e
capacidadePassageiros,   e   um   método   abstrato
calcularCustoOperacional()   que   retorna   o   custo   por
quilômetro.   

Crie   as   subclasses   Onibus,   com   o   atributo
consumoPorKm   (litros/km),   e   Metro,   com
consumoEnergiaPorKm   (kWh/km).   Cada   uma   deve
implementar o cálculo do custo com valores fictícios: R$ 6,00
por litro de diesel e R$ 0,80 por kWh. 

Na função principal, permita   criar   objetos   dos   dois   
tipos   e   exibir   os   custos
operacionais usando polimorfismo. Implemente tratamento de
exceções para validar os dados de entrada: placa não pode
ser vazia, e os valores numéricos devem ser positivos.

'''

from abc import ABC, abstractmethod

class VeiculoTransporte(ABC): # ABC = Abstract Base Class.
    def __init__(self, placa, capacidadePassageiros):
        self.placa = placa
        self.capacidadePassageiros = capacidadePassageiros
        
    # até aqui apenas armazenamos informações.

    @abstractmethod
    def calcularCustoOperacional(self):
        pass

    # pass porque cada "filho" fará o seu calculo 

class Onibus(VeiculoTransporte):
    # herdar o conteudo do pai 
    def __init__(self, placa, capacidadePassageiros, consumokm):
        super().__init__(placa, capacidadePassageiros) # usar o construtor do pai
        self.consumokm = consumokm 

    def calcularCustoOperacional(self):
        return self.consumo_por_km * 6.0

class Metro(VeiculoTransporte):
    def __init__(self, placa, capacidadePassageiros, consumoenergiakm):
        super().__init__(placa, capacidadePassageiros)
        self.consumoenergiakm = consumoenergiakm

    def calcularCustoOperacional(self):
        return self.consumo_energia_por_km * 0.80

def main():

    veiculos = []

    while True:
        print("\n===Menu===\n")
        print("\n1. Cadastrar Onibus")
        print("2. Cadastrar Metro")
        print("3. Mostrar Custos Operacionais")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ").strip().lower()

        if opcao == "1":
            print("\nCadatsro de Onibus\n")

            try:
                placa = input("Placa: ")

                if placa.strip() == "":
                        raise ValueError("\nA Placa não pode estar Vazia.\n")
                
                capacidadePassageiros = int(input("Capacidade de Passageiros: "))

                if capacidadePassageiros <=0:
                    raise ValueError("\nA capacidade deve ser POSITIVA.\n")

                consumo = float(input("\nConsumo por km (litros/km): "))

                if consumo <= 0:
                    raise ValueError("O consumo deve ser POSITIVO.")

                veiculos.append(Onibus(placa, capacidadePassageiros, consumokm = consumo))

                print("\nOnibus cadastrado com Sucesso.\n")

            except ValueError as e:
                print(f"Erro: {e}")
                
        elif opcao == "2":

            print("\nCadastro de Metro\n")

            try:
                placa = input("Indentificação: ")
            
                if placa.strip() == "":
                    raise ValueError("\nA Indentificação não pode estar Vazia.\n")
                            
                capacidadePassageiros = int(input("Capacidade de Passageiros: "))
            
                if capacidadePassageiros <=0:
                    raise ValueError("\nA capacidade deve ser POSITIVA.\n")
            
                consumo = float(input("\nConsumo por km (KwH/km): "))
            
                if consumo <= 0:
                    raise ValueError("O consumo deve ser POSITIVO.")
            
                veiculos.append(Onibus(placa, capacidadePassageiros, consumoenergiakm = consumo))

                print("\nMetro cadastrado com Sucesso.\n")
                
            except ValueError as e:
                            print(f"Erro: {e}")


        elif opcao == "3":

        # POLIMORFISMO 

            if not veiculos:
                print("\nNenhum Veiculo Cadastrado.\n")
            else:
                print("\n---Custos Operacionais por Km---\n")
                for veiculo in veiculos:
                     tipo = "Onibus" if isinstance(veiculo, Onibus) else "Metro"
                     custo = veiculo.calcularCustoOperacional()
                     print(f"{tipo} - {veiculo.placa}: R$ {custo:.2f} por km")
                     print()

        elif opcao == "0":
            print("\nObrigada por Utilizar os nossos Serviços. Volte Sempre.\n")
            break

        else:
            print("\nOpção Invalida, Digite uma opção Válida.\n")
            continue

if __name__ == "__main__":
    main()