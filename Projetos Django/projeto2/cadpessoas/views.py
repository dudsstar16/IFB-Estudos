
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter  # 1. Importa o filtro de ordenação
from .models import Pessoas
from .serializers import PessoasSerializer

class PessoasViewSet(viewsets.ModelViewSet):
    queryset = Pessoas.objects.all()
    serializer_class = PessoasSerializer
    
    # 2. Habilita o recurso de ordenação dinâmica
    filter_backends = [OrderingFilter]
    
    # 3. Campos permitidos para ordenação
    ordering_fields = ['id', 'nome', 'cidade']
    
    # 4. Ordenação padrão inicial (ex: por id crescente)
    ordering = ['id']

    # Permite somente consultas
    http_method_names = ['get', 'head']
