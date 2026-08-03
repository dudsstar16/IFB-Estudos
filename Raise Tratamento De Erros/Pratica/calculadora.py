
## 100% ORIENTADO A OBJETOS - TUDO DENTRO DE CLASSE


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

            if opcao == "5":
                print("\nSaindo da Calculadora. Até Logo!\n")
                break

            if opcao not in {"1", "2", "3", "4"}:
                print("\nOpção Inválida. Por favor, escolha entre 1 e 5.\n")
                continue 

            try:
                a = float(input("\nDigite o Primeiro número: "))
                b = float(input("\nDigite o Segundo número: "))

                if opcao == "1":
                    resultado = self.calc.soma(a, b)
                elif opcao == "2":
                    resultado = self.calc.subtracao(a, b)
                elif opcao == "3":
                    resultado = self.calc.multiplicacao(a, b)
                elif opcao == "4":
                    resultado = self.calc.divisao(a, b)

                print(f"\nResultado: {resultado}\n")

            except ValueError:
                print("\nErro: Por favor, digite um número Válido.\n")
            except ZeroDivisionError as e: # pegar a mensagem do rase, por isso o e no final 
                print(f"\nErro: {e}.\n")


if __name__ == "__main__":
    interface = Interface()
    interface.menu()