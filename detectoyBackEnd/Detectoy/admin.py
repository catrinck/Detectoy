from django.contrib import admin
from .models import Gerente, Funcionario, ErroDetectado

# Register your models here.

admin.site.register(ErroDetectado)
admin.site.register(Funcionario)
admin.site.register(Gerente)
