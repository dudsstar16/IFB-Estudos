
import psycopg2

class ProdutoModel:
    def __init__(self):
        try:
            self.conexao = psycopg2.connect(
                host="localhost",   
                database="produtosdb",
                user="postgres",
                password="alunocceia"
            )
        except psycopg2.Error as e:
            print(f"\nErro ao conectar ao banco: {e}")


    def listar_produtos(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT * FROM produtos")
            produtos = cursor.fetchall()
            cursor.close()
            return produtos
        except psycopg2.Error as e:
            print(f"\nErro ao listar produtos: {e}")
            return []

    def cadastrar_produto(self, nome, preco):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("INSERT INTO produtos (nome, preco) VALUES (%s, %s)", (nome, preco))
            self.conexao.commit()
            cursor.close()
        except psycopg2.Error as e:
            print(f"\nErro ao cadastrar produto: {e}")

    def atualizar_produto(self, id, nome, preco):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("UPDATE produtos SET nome = %s, preco = %s WHERE id = %s", (nome, preco, id))
            self.conexao.commit()
            cursor.close()
        except psycopg2.Error as e:
            print(f"\nErro ao atualizar produto: {e}")

    def deletar_produto(self, id_produto):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
            self.conexao.commit()
            cursor.close()
        except psycopg2.Error as e:
            print(f"\nErro ao deletar produto: {e}")


    