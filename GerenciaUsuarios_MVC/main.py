
from controller.usuario_controller import UsuarioController
from views.usuario_view import menu_principal, mensagem 

def main():
    controller = UsuarioController()

    while True:
        try:
            opcao = menu_principal()

            if opcao == "1":
                controller.listar() 
            elif opcao == "2":
                controller.cadastrar()
            elif opcao == "3":
                controller.atualizar()
            elif opcao == "4":
                controller.excluir()
            elif opcao == "0":
                mensagem("Saindo do sistema...")
                break
            else:   
                mensagem("\n❌ Opção inválida. Por favor, escolha uma opção válida.")
        except Exception as e:  
            mensagem(f"\n❌ Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
    