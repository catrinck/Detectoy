from rest_framework import serializers
from .models import Gerente, Usuario

class GerenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gerente
        exclude = ['senha']


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['senha']