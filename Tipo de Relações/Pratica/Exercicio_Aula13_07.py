## exercicios treinar as quatro relações 
## sem menu
## gerar exemplos na main
## associação, agregação, comparação, dependencia

class Biblioteca:

    def __init__(self, nomeautor, responsavel): # COMPOSIÇÃO: responsavel por criar e armazenar os livros (FORTE)
        self.__nomeautor = nomeautor
        self.__responsavel = responsavel

    def get_nomeautor(self):
        return self.__nomeautor
    
    def get_responsavel(self):
        return self.__responsavel
    
    def set_nomeautor(self, nomeautor):
        self.__nomeautor = nomeautor 
    
    def set_responsavel(self, nomeautor, responsavel):
        if not nomeautor:
            return nomeautor.lower() == responsavel.lower()
        else:
            False
                


class Livro:

    def __init__(self, titulo, ano): # criar uma AGREGAÇÃO em referencia ao Autor (MAIS FRACA QUE COMPOSIÇÃO)



class Autor:

    def __init__(self, nome, nacionalidade):





class Usuario:

    def __init__(self, nome, ): # ASSOCIAÇÃO, possuir referencia a biblioteca ao qual está associado (ESTAVEL)
                                # metodo para pegar livro emprestado, mas sem armazena-lo, DEPENDENCIA (MUITO FRACA)



