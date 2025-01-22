from rest_framework import serializers
from .models import Gerente, Usuario


class CriarGerenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gerente
        fields = '__all__'


class GerenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gerente
        exclude = ['senha']

class LoginGerenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gerente
        fields = ['email', 'senha']

class CriarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['senha']