from django.shortcuts import render
from .models import Aluno

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'gestao/lista_alunos.html', {'alunos': alunos})