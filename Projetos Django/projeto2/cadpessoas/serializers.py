
from rest_framework import serializers  # ferramentas do DRF para (de)serializar
from .models import Pessoas  # modelo Pessoas do app

# Serializer para o modelo Pessoas — converte instâncias <-> representações JSON/HTTP
class PessoasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoas
        fields = '__all__'  # expõe todos os campos do modelo Pessoas
