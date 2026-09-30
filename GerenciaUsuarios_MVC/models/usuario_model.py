
import psycopg2

class UsuarioModel:
    def __init__(self):
        try:
            self.conexao = psycopg2.connect(
                host="localhost", # servidor local
                database="usariosbd", # nome do database
                user="postgres", # nome do usuário
                password="alunocceia"
            )
        except Exception as e:
            print("\n❌Erro ao se conectar ao banco:", e) # so fecha a conexao na main

    def listar_usuarios(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT id, nome, email FROM usarios ORDER BY id;")
            usuarios = cursor.fetchall() # pegar todo o resultado da consulta
            cursor.close() # fechar o cursor 
            return usuarios
        except Exception as e:
            print("\n❌ Erro ao listar usuários:", e)
            return []

    def inserir_usuario(self, nome, email):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("INSERT INTO usarios (nome, email) VALUES (%s, %s);", (nome, email))
            self.conexao.commit() # confirmar a transação
            cursor.close()
        except Exception as e:
            print("\n❌ Erro ao inserir usuário:", e)
            self.conexao.rollback() # so se usa com INSERT, UPDATE ou DELETE

    def atualizar_usuario(self, id_usuario, nome, email):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("UPDATE usarios SET nome = %s, email = %s WHERE id = %s;", (nome, email, id_usuario))
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("\n❌ Erro ao atualizar usuário:", e)
            self.conexao.rollback()

    def excluir_usuario(self, id_usuario):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM usarios WHERE id = %s;", (id_usuario,))
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("\n❌ Erro ao excluir usuário:", e)
            self.conexao.rollback()

