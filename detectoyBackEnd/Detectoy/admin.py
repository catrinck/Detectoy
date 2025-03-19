from django.contrib import admin
from .models import Gerente, Funcionario, Erro

# Register your models here.

admin.site.register(Erro)
admin.site.register(Funcionario)
admin.site.register(Gerente)
