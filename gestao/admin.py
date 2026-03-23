from django.contrib import admin

from .models import Oficina, Aluno

# Isso faz as tabelas aparecerem no painel de controle
admin.site.register(Oficina)
admin.site.register(Aluno)