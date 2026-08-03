## Exe 04 

## REVISAO = encapulsamento (metodos privados)
## set faz verificação (IMPORTANTE)

class Produto:

    def __init__(self, nome, preco, quantidade):
        self.__nome = nome 
        self.__preco = preco
        self.__quantidade = quantidade


    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade

    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco

    def set_quantidade(self, quantidade):
        if quantidade >= 0:
            self.__quantidade = quantidade

    def calcular_total(self): # total do carrinho vai chamar para calcular os valores no carrinho
        return self.__preco * self.__quantidade

class carrinho_de_compras:

    def __init__(self): # lista de produtos vazias
        self.produtos = []

    def add_produtos(self, produto):
        self.produtos.append(produto) # adicionar o produto a lista

    def remover_produtos(self, nome):
        for produto in self.produtos: # para produto dentro da lista de produtos
            if produto.get_nome().lower == nome.lower(): # get para buscar o nome do produto
                self.produtos.remove(nome) # entao remove
                return True 
        return False # não achou o produto 

    def listar_produtos(self): # pecorrer a lista, nao precisa de parametro, pois a lista ja esta na classe
        if self.produtos == 0:
            print("Carrinho Vazio")
        else:
            print("\nSegue Abaixo os Produtos Listados no Carrinho, para conferencia...\n")
            print("=" * 50)
            for produtos in self.produtos:
                print(f"\n- Nome: {produtos.get_nome()}, Preço: R$ {produtos.get_preco():.2f}, Quantidade: {produtos.get_quantidade()}")
            print()

    def calcular_total(self):
        total = 0 
        for produtos in self.produtos:
            total += produtos.calcular_total() # chamar a funcao para calcular o total 
            return total # retorna o total de cada produto e vai em loop ate o limite 


def main():

    carrinho = carrinho_de_compras() # instanciar usar o mesmo carrinho, o menu usar o mesmo objeto

    while True:
        print("=" * 50)
        print("\nBem vindo(a) ao menu do seu carrinho !!! :D\n")
        print("=" * 50)
        print("\n1. Adicionar Produto")
        print("\n2. Remover Produto")
        print("\n3. Listar Produtos")
        print("\n4. Calcular o Total do carrinho")
        print("\n5. Sair")

        opcao = input("\nEscolha a opção desejada: ")

        if opcao == "1":
            nome = input("Insira o nome do Produto: ")
            preco = float(input("Insira o preço do Produto: "))
            quantidade = int(input("Insira a quantidade desejada: "))
            produto = Produto(nome, preco, quantidade)
            carrinho.add_produtos(produto)
            print("\nProduto Adicionado com Sucesso...\n")
            
        elif opcao == "2":
            nome = input("Qual Produto voce deseja remover: ")
            if carrinho.remover_produtos(nome) == True:
                print("\nProduto removido\n")
            else:
                print("\nProduto Inexistente\n")

        elif opcao == "3":
            carrinho.listar_produtos()
 
        elif opcao == "4":
            total = carrinho.calcular_total()
            print(f"\nO total do carrinho foi equivalente a: R${total}\n")
            print("=" * 50)
            print("\nSegue Abaixo os Produtos Listados no Carrinho, para conferencia...\n")
            print("=" * 50)
            for produtos in carrinho.produtos:
                print(f"- Nome:{produtos.get_nome()}, Preço: R${produtos.get_preco():.2f}, Quantidade:{produtos.get_quantidade()}")
                print()

        elif opcao == "5":
            print("\nEncerrando o programa...\n")
            print("\nObrigada por Utilizar os nossos Serviços...\n")
            print("\nVolte Sempre :D\n")
            break 
        else:
            print("\nOpção inválida...")
            print("\nTente Novamente !!!")


if __name__ == "__main__":
    main()