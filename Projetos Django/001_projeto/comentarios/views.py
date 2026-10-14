
# Create your views here.

from django.shortcuts import render, redirect # atalhos para renderizar templates e redirecionar
from .models import Comentario # modelo Comentario usado para persistência

# View para salvar um comentário e mostrar o formulário/lista de comentários

def salvar_comentario(request):
 
 # Se o método for POST, processa o envio do formulário

 if request.method == 'POST':
    autor = request.POST.get('autor') # obtém o valor do campo 'autor' (pode ser None)

    texto = request.POST.get('texto') # obtém o valor do campo 'texto'

    comentario = Comentario(autor=autor, texto=texto) # cria instância do modelo

    comentario.save() # salva no banco de dados

    # Redireciona para a mesma view (padrão PRG - Post/Redirect/Get) para evitar reenvio do formulário

    return redirect('salvar_comentario')

 # Se não for POST (normalmente GET), recupera todos os comentários ordenados do mais recente ao mais antigo
 comentarios = Comentario.objects.all().order_by('-data_criacao')

 # Renderiza o template passando os comentários no contexto

 return render(request, 'comentarios/formulario.html', {'comentarios': comentarios})

