from django.db import models

# Tabela para as Oficinas (Breaking, DJ, Graffiti, etc)
class Oficina(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Tabela para os Alunos
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    oficinas = models.ManyToManyField(Oficina)

    def __str__(self):
        return self.nome


# Tabela para registrar as Faltas e Presenças
class Presenca(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)
    data = models.DateField()
    presente = models.BooleanField(default=True)

    def __str__(self):
        status = "Presente" if self.presente else "Faltou"
        return f"{self.aluno.nome} - {self.oficina.nome} ({self.data}): {status}"