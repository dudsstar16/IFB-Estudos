#==========================================

#MENU DE FUNÇÕES PARA GERENCIADOR DE TAREFAS

#==========================================

from dever08_06 import adicionar_tarefa, lista_ordenada, tarefa_concluida

#==========================================

#MENU DE OPÇÕES 

#==========================================

lista_tarefas = []

def mostrar_menu():
    
    while True:
        print("\nBEM VINDO AO GERENCIADOR DE TAREFAS! :D\n")
        print("\n============================")
        print("\nMENU DE OPÇÕES\n")
        print("\n============================")
        print("\n1. Adicionar tarefa")
        print("\n2. Listar tarefas ordenadas por prioridade")
        print("\n3. Marcar tarefa como concluida")
        print("\n4. Sair")

        escolha = input("\nDigite o numero da opcao desejada: ")

        if escolha == "1":
            print("\nAdicionando nova tarefa...")
            adicionar_tarefa(lista_tarefas)
        elif escolha == "2":
            print("\nLista de tarefas:")
            lista_ordenada(lista_tarefas)
        elif escolha == "3":
            print("\nMarcar tarefa como concluida...")
            tarefa_concluida(lista_tarefas)
        elif escolha == "4":
            print("\nObrigada por utiluzar o gerenciador de tarefas! Ate a proxima! :D\n")
            break
        else:
            print("\nOpcao invalida. Por favor, tente novamente.")


if __name__ == "__main__":
    mostrar_menu()



