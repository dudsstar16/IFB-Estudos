
from models.usuario_model import UsuarioModel
from views.usuario_view import * 

class UsuarioController:
    def __init__(self):
        self.model = UsuarioModel()

    def listar(self):
        try:
            usuarios = self.model.listar_usuarios()
            mostrar_usuarios(usuarios)
        except Exception as e:  
            mensagem(f"\n❌ Erro ao listar usuários: {e}")

    def cadastrar(self):
        try:
            nome, email = solicitar_dados_usuario()
            if not nome or not email:
                mensagem("\n❌ Nome e e-mail são obrigatórios!")
                return
            self.model.inserir_usuario(nome, email)
            mensagem("\n✅ Usuário cadastrado com sucesso!")
        except Exception as e:
            mensagem(f"\n❌ Erro ao cadastrar usuário: {e}")

    def atualizar(self):
        try:
            id_usuario = solicitar_id()
            if id_usuario is None:
                return
            nome, email = solicitar_dados_usuario()
            self.model.atualizar_usuario(id_usuario, nome, email)
            mensagem("\n✏️ Usuário atualizado com sucesso!")
        except Exception as e:
            mensagem(f"\n❌ Erro ao atualizar usuário: {e}")

    def excluir(self):
        try:
            id_usuario = solicitar_id()
            if id_usuario is not None: 
                self.model.excluir_usuario(id_usuario)
            mensagem("\n🗑️ Usuário excluído com sucesso!")
        except Exception as e:
            mensagem(f"\n❌ Erro ao excluir usuário: {e}")


