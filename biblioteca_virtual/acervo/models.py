from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)
    arquivo_pdf = models.FileField(upload_to='livros_pdf/')
    capa = models.ImageField(upload_to='capas/', blank=True, null=True)
    uploader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo