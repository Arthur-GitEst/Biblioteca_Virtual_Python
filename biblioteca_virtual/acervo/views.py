from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Livro

@login_required
def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'acervo/lista_livros.html', {'livros': livros})

@login_required
def ler_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    # A URL do PDF estará disponível no template através de {{ livro.arquivo_pdf.url }}
    return render(request, 'acervo/ler_livro.html', {'livro': livro})
