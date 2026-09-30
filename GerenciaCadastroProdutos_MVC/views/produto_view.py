
def menu_produto():
    print("\n===== Menu Produto =====")
    print("1. Listar Produtos")
    print("2. Cadastrar Produto")
    print("3. Atualizar Produto")
    print("4. Deletar Produto")
    print("5. Sair do Sistema")
    return input("\nEscolha uma opção: ")

def mostrar_produtos(lista):
    print("\n===== Lista de Produtos =====")
    if not lista:
        print("\nNenhum produto cadastrado.")
    else:
        for produto in lista:
            print()
            print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: {produto[2]}")

def solicitar_dados_produto():
    print("\n===== Cadastrar Produto =====")
    nome = input("Digite o nome do produto: ")
    preco = input("Digite o preço do produto: ")
    return nome, preco

def solicitar_id_produto():
    try:
        return int(input("\nDigite o ID do produto: "))
    except ValueError:
        print("\nID inválido. Por favor, digite um número inteiro.")
        return None

def mensagem(acao):
    print(f"\nProduto {acao} com sucesso!")
