
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('comentarios.urls')), # Inclui as URLs do app 'comentarios' na raiz do projeto
]
