
from rest_framework.routers import DefaultRouter
from .views import PessoasViewSet

router = DefaultRouter()

router.register(r'', PessoasViewSet, basename='pessoas')  # registra o ViewSet para o recurso Pessoas

urlpatterns = router.urls