class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao (self, a, b):
        if b == 0:
            raise ZeroDivisionError("\nNão é possivel dividir por zero.\n")
        return a / b


class Interface:
    def __init__(self):
        self.calc = Calculadora()

    def menu(self):
        while True:
            print("\n====Calculadora Simples===")
            print("1. Soma")
            print("2. Subtração")
            print("3. Multiplicação")
            print("4. Divisão")
            print("5. Sair")

            opcao = input("\nEscolha uma opção: ").strip()

            try