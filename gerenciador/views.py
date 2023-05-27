from django.shortcuts import render
from django.http import HttpResponse
from locadora.models import Filme,Locacao, Cliente

def index (request):
    cliente = Cliente.objects.all()
    context = {"cliente": cliente}
    return render (request, "locadora/index.html",context)

def lista_locacao (request):
    lista_locacao = Locacao.objects.all()
    context = {"locacoes": lista_locacao}
    return render (request, "locadora/lista_locacao.html", context)

def filme(request):
    filmes = Filme.objects.all()
    context = {"filmes": filmes}
    return render (request, "locadora/filmes.html",context)