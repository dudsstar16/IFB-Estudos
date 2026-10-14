
# Rota raiz do app 'comentarios':
# - GET -> exibe o formulário e a lista de comentários
# - POST -> envia o formulário e salva um novo comentário (a view faz PRG: redireciona após POST)

from django.urls import path
from .views import salvar_comentario
urlpatterns = [
 path('', salvar_comentario, name='salvar_comentario'),
]
