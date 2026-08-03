class Livro:    

    def __init__(self, titulo, autor, id_livro):
        self.__titulo = titulo 
        self.__autor = autor
        self.__id_livro = id_livro


    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_id_livro(self):
        return self.__id_livro

    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    def set_autor(self, novo_autor):
        self.__autor = novo_autor

    def set_id_livro(self, novo_id_livro):
        self.__id_livro = novo_id_livro


class Usuario:

    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula 
        self.__livros_emprestados = [] # criar metodo para inserção de dados

    def get_nome(self):
        return self.__nome
    
    def get_matricula(self):
        return self.__matricula
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_matricula(self, nova_matricula):
        self.__matricula = nova_matricula

    
    def emprestar_livros(self, livro):
        self.__livros_emprestados.append(livro) # adicionando na lista de livros emprestados
        print(f"\n{self.__nome} pegou emprestado o livro '{livro.get_titulo()}'.\n")

    def devolver_livros(self, id_livro):
        for livro in self.__livros_emprestados: # pecorre a lista
            if livro.get_id_livro () == id_livro: # verifica o id livro, pegando um por um na lista 
                self.__livros_emprestados.remove(livro) # remove o livro da lista
                print(f"\n{self.__nome} devolveu o livro '{livro.get_titulo()}'.\n")
                return # imprime e sai, acaba o metodo 
        
        print(f"\n{self.__nome} não possui um livro com ID {id_livro}\n") 

    def listar_livros_emprestados(self):
        if not self.__livros_emprestados:
            print("\nNenhum livro emprestado.\n")
        else:
            print("\nLivros emprestados:\n")
            for livro in self.__livros_emprestados: 
                print(f"- {livro.get_titulo()} ({livro.get_id_livro()})")
            print()

            
def main():

     # tarefa de casa menu: (cadastrar livro, usuario, emprestar livro, devolver livro e listar livros emprestados)


    while True:
        print("\nBEM VINDO AO SISTEMA DA BIBLIOTECA! :D\n")
        print("\n============================")
        print("\nMENU DE OPÇÕES\n")
        print("\n============================")
        print("\n1. Cadastrar Livro")
        print("\n2. Registrar um Usuario")
        print("\n3. Realizar um emprestimo de Livro")
        print("\n4. Devolver um Livro")
        print("\n5. Listar Livros Emprestados")
        print("\n6. Sair")

        escolha = input("\nDigite o numero da opcao desejada: ")

        if escolha == "1":
            print("\nCadastrando Livro...")
            adicionar_tarefa(lista_tarefas)
        elif escolha == "2":
            print("\nRegistrando o Usuario Inserido...")
            lista_ordenada(lista_tarefas)
        elif escolha == "3":
            print("\nRealizando um Emprestimo de Livro...")
            tarefa_concluida(lista_tarefas)
        elif escolha == "4":
            print("\nRealizando a Devolução do Livro...")
            tarefa_concluida(lista_tarefas)
        elif escolha == "5":
            print("\nLivros Emprestados:")
            tarefa_concluida(lista_tarefas)    
        elif escolha == "6":
            print("\nObrigada por utiluzar o nosso sistema de Biblioteca! Ate a proxima! :D\n")
            break
        else:
            print("\nOpcao invalida. Por favor, tente novamente.")

    livro1 = Livro("O Pequeno Principe", "Antoine de Saint-Exupéry", 1) # inserindo os objetos na classe Livros
    livro2 = Livro("Capitões da Areia", "Jorge Amado", 2) # inserindo os objetos na classe Livros

    usuario1 = Usuario("Clara", "2026001")

    usuario1.emprestar_livros(livro1) # pegou emprestado o livro 1 e 2, a Clara
    usuario1.emprestar_livros(livro2)

    usuario1.listar_livros_emprestados() # listou os livros dela

    usuario1.devolver_livros(1) # devolveu o livro1

    usuario1.listar_livros_emprestados() # listou a lista de livros dela atualizada


 # tarefa de casa menu: (cadastrar livro, usuario, emprestar livro, devolver livro e listar livros emprestados)


if __name__ == "__main__":
    main()