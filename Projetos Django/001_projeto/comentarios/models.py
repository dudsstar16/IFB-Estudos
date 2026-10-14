
# Create your models here.

from django.db import models

# Modelo que representa um comentário simples

class Comentario(models.Model):
 autor = models.CharField(max_length=100) # nome do autor do comentário (campo de texto curto)
 texto = models.TextField() # conteúdo do comentário (texto livre)
 data_criacao = models.DateTimeField(auto_now_add=True) # data/hora de criação preenchida automaticamente
    
 def __str__(self):

 # Representação legível do objeto: "Autor: texto..." (mostra os primeiros 30 caracteres)

    return f"{self.autor}: {self.texto[:30]}" # [:30] limita a exibição para não mostrar o comentário completo
