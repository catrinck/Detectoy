import bcrypt
import os

from django.conf import settings
from django.db import models
from django.utils import timezone


class Gerente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, primary_key=True)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.senha = bcrypt.hashpw(bytes(self.senha, 'utf-8'), bcrypt.gensalt())
        super(Gerente, self).save(*args, **kwargs)


# Os campos cameras e relatorios sao referentes as permissoes do usuario
# Se camera == True entao ele tem acesso aos comandos da camera
# O mesmo para relatorios
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, primary_key=True)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)
    log = models.BooleanField(default=False)
    cameras = models.BooleanField(default=False)
    relatorios = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.senha = bcrypt.hashpw(bytes(self.senha, 'utf-8'), bcrypt.gensalt())
        super(Funcionario, self).save(*args, **kwargs)


class Erro(models.Model):
#   def image_file_name(self, filetype=".jpg"):
#       return str(self.tipo) + "-" + str(self.linha) + "_" + self.momento.strftime("%Y-%m-%d-%H-%M-%S-%f") + filetype

    momento = models.DateTimeField(default=timezone.now)
    linha = models.IntegerField()
    tipo = models.IntegerField()
    tela_quebrada = models.BooleanField()
    carcaca_quebrada = models.BooleanField()
    imagem = models.FilePathField(path=os.path.join(os.path.dirname(__file__), "images"))

    def __str__(self):
        return self.imagem

#   def save(self, *args, **kwargs):
#       self.imagem = Erro.image_file_name(self)
#       super(Erro, self).save(*args, **kwargs)
