from django.shortcuts import get_object_or_404, render
from .models import Receita


def index(request):
    receitas = Receita.objects.all()

    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    mostrar_receita = {
        'receita': receita
    }

    return render(request, 'receita.html', mostrar_receita)
