
# Rota raiz do app 'comentarios':
# - GET -> exibe o formulário e a lista de comentários
# - POST -> envia o formulário e salva um novo comentário (a view faz PRG: redireciona após POST)

from django.urls import path, include  # funções para definir rotas e incluir outras rotas
from rest_framework.routers import DefaultRouter # router para ViewSets
from .views import salvar_comentario, ComentarioViewSet # views do app

router = DefaultRouter()
router.register(r'comentarios', ComentarioViewSet) # registra o ViewSet em /api/

urlpatterns = [
    path('', salvar_comentario, name='salvar_comentario'), # formulário/lista (GET) e salva (POST)
    path('', include(router.urls)), # inclui rotas da API geradas pelo router (ex.: /comentarios/, /comentarios/<pk>/)
]
