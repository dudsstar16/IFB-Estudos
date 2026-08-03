'''
 Crie um programa que simule o funcionamento de um caixa
eletrônico. O usuário inicia com um saldo fictício e pode
realizar as seguintes operações através de um menu iterativo:
1.Consultar saldo
2.Depositar dinheiro
3.Sacar dinheiro
4.Sair
● O programa deve repetir o menu até o usuário escolher a
opção 4 (sair).
'''

print("\n======= BEM-VINDO AO SISTEMA =======")

saldo = 5000.00
print(f"\nSaldo Atual {saldo}")

while True:
    print("\nSelecione uma opção:")
    print("\n1 - Consultar saldo")
    print("\n2 - Depositar dinheiro")
    print("\n3 - Sacar dinheiro")
    print("\n4 - Sair")

    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":
        print(f"\nSaldo atual: R$ {saldo:.2f}")

    elif opcao == "2":
        valor = float(input("\nDigite o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            print(f"\nDepósito realizado com sucesso!")
            print(f"\nNovo saldo: R$ {saldo:.2f}")
        else: 
            print("\nValor Inválido!")

    elif opcao == "3":
        valor = float(input("\nDigite o valor do saque: R$ "))

        if valor <= saldo:
            saldo -= valor
            print(f"\nSaque realizado com sucesso!")
            print(f"\nNovo saldo: R$ {saldo:.2f}")
        else:
            print("\nSaldo insuficiente para realizar o saque.")

    elif opcao == "4":
        print("\nObrigado por utilizar o sistema. Até logo!")
        break

    else:
        print("\nOpção inválida. Tente novamente.")

