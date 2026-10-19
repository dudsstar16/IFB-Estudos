
from rest_framework import serializers  # ferramentas do DRF para (de)serializar objetos
from .models import Comentario  # importa o modelo Comentario do mesmo app

# Serializer que converte instâncias de Comentario <-> representações JSON/HTTP
# Utiliza ModelSerializer para gerar automaticamente os campos com base no modelo
class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario  # modelo/tabela alvo do serializer
        fields = '__all__'  # expõe todos os campos do modelo/tabela no endpoint
        