from django.contrib import admin
from django.urls import path
from gestao.views import lista_alunos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', lista_alunos, name='lista_alunos'),
]