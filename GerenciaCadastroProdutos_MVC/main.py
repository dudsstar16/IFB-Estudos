
from controller.controller_produto import ProductController
from views.produto_view import menu_produto, mensagem

def main():
    controller = ProductController()

    while True:
        try:
            opcao = menu_produto()
            
            if opcao == "1":
                controller.listar_produtos()
            elif opcao == "2":
                controller.cadastrar_produto()
            elif opcao == "3":
                controller.atualizar_produto()
            elif opcao == "4":
                controller.deletar_produto()
            elif opcao == "5":
                mensagem("\nSaindo do sistema...")
                break
            else:
                mensagem("\nOpção inválida. Por favor, escolha uma opção válida.")
        except Exception as e:
            mensagem(f"\nOcorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
