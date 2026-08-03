'''
Você vai criar um programa que gerencia uma lista de tarefas. O
programa deve:
1. Permitir que o usuário adicione tarefas. Cada tarefa deve ter:
Descrição (string), Prioridade (inteiro de 1 a 5, onde 1 é a
prioridade mais alta) e Status (inicialmente “pendente”);
2. Armazenar cada tarefa como um dicionário com as chaves
"descrição", "prioridade" e "status";
3. Manter todas as tarefas numa lista;
4. Criar funções para: Adicionar tarefas, Mostrar todas as tarefas
ordenadas por prioridade (da maior para a menor) e Marcar
uma tarefa como concluída (alterar o status para
“concluída”);
5. Criar uma função main() que permita ao usuário escolher
opções num menu para: Adicionar tarefa, Listar tarefas,
Marcar tarefa como concluída e Sair do programa.
'''

#==========================================

#FUNÇÃO ADICIONAR TAREFA

#==========================================


def adicionar_tarefa(lista_tarefas):

        descricao = input(f"\nDigite a descrição da tarefa: ")
        print("\n============================")
        print("\n============================")
        prioridade = int(input(f"\nDigite a prioridade da tarefa (1-5): "))
        print("\n============================")
        print("\n============================")

        tarefa = {
            "descrição": descricao, 
            "prioridade": prioridade, 
            "status": "pendente",
            "codigo": len(lista_tarefas) + 1
        }

        lista_tarefas.append(tarefa)    

        print(f"\nTarefa, referente a {descricao} adicionada com sucesso!")

'''
4. Criar funções para: Mostrar todas as tarefas
ordenadas por prioridade (da maior para a menor) e Marcar
uma tarefa como concluída (alterar o status para
“concluída”);
5. Criar uma função main() que permita ao usuário escolher
opções num menu para: Adicionar tarefa, Listar tarefas,
Marcar tarefa como concluída e Sair do programa.
'''

#==========================================

#FUNÇÃO ORDENAR TAREFAS POR PRIORIDADE

#==========================================


def lista_ordenada(lista_tarefas):
        lista_tarefas.sort(lambda t: t["prioridade"])
        print("\nTarefas ordenadas por prioridade (da maior para a menor):")
        for t in lista_tarefas:
            print("\nStatus da tarefa:", t["status"])
            print("\nPrioridade da tarefa:", t["prioridade"])
            print("\nDescrição da tarefa:", t["descrição"])
            print("\nCódigo da tarefa:", t["codigo"])
            print("\n============================")
            print("\n============================")

#==========================================

#FUNÇÃO MARCAR TAREFA COMO CONCLUÍDA

#==========================================


def tarefa_concluida(lista_tarefas):
    codigo = int(input("\nDigite o código da tarefa a ser marcada como concluída: "))
    for c in lista_tarefas:
        if c["codigo"] == codigo:
            c["status"] = "concluída"
            print(f"\nTarefa, referente a {c['descrição']} marcada como concluída!")
            return
    print("\nCódigo de tarefa não encontrado. Por favor, tente novamente.")






