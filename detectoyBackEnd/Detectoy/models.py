from django.db import models


class Gerente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.BigIntegerField(primary_key=True)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# Os campos cameras e relatorios sao referentes as permissoes do usuario
# Se camera == True entao ele tem acesso aos comandos da camera
# O mesmo para relatorios
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.BigIntegerField(primary_key=True)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)
    cameras = models.BooleanField(default=False)
    relatorios = models.BooleanField(default=False)

    def __str__(self):
        return self.nome