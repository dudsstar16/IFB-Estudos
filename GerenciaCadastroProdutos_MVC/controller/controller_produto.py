
from models.produto_model import ProdutoModel 
from views.produto_view import *

class ProdutoController:
    def __init__(self):
        self.model = ProdutoModel()

    def listar_produtos(self):
        try:
            produtos = self.model.listar_produtos()
            mostrar_produtos(produtos)
        except Exception as e:
            print(f"\nErro ao listar produtos: {e}")

    def cadastrar_produto(self):
        try:
            nome, preco = solicitar_dados_produto()
            if not nome or not preco:
                print("\nNome e preço do produto não podem ser vazios.")
                return
            self.model.cadastrar_produto(nome, preco)
            mensagem("\nProduto cadastrado com sucesso!")
        except Exception as e:
            print(f"\nErro ao cadastrar produto: {e}")

    def atualizar_produto(self):
        try:
            id_produto = solicitar_id_produto()
            if id_produto is None:
                return
            nome, preco = solicitar_dados_produto()
            self.model.atualizar_produto(id_produto, nome, preco)
            mensagem("\nProduto atualizado com sucesso!")
        except Exception as e:
            print(f"\nErro ao atualizar produto: {e}")

    def deletar_produto(self):
        try:
            id_produto = solicitar_id_produto()
            if id_produto is not None:
                self.model.deletar_produto(id_produto)
                mensagem("\nProduto deletado com sucesso!")
        except Exception as e:
            print(f"\nErro ao deletar produto: {e}")

