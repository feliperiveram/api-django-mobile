from django.urls import path
from rest_usuario.views import listar_usuarios

urlpatterns = [
    path('listar_usuarios',listar_usuarios,name="listar_usuarios"),
]
