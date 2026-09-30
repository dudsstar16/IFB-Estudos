
def menu_principal():
    print()
    print(("="*5) + " MENU PRINCIPAL " + ("="*5))
    print("1. Listar usuários")
    print("2. Cadastrar usuário")
    print("3. Atualizar usuário")
    print("4. Excluir usuário")
    print("0. Sair")
    return input("\nEscolha uma opção: ")

def mostrar_usuarios(lista):
    print()
    if not lista:
        print("\n❌ Nenhum usuário encontrado.")
    else:
        for usuario in lista:
            print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Email: {usuario[2]}")
            print()

def solicitar_dados_usuario(): 
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    return nome, email

def mensagem(texto):
    print(texto) # pra imprimir mensagens de sucesso 

def solicitar_id():
    try:
        return int(input("Informe o ID do usuário: "))
    except ValueError:
        print("\n❌ ID inválido. Por favor, insira um número inteiro.")
        return None


