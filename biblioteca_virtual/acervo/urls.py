from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),
    path('livro/<int:livro_id>/', views.ler_livro, name='ler_livro'),
]