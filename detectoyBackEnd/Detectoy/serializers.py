from rest_framework import serializers
from .models import Gerente, Funcionario, Erro


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


class CriarFuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        exclude = ['senha']


class ErroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Erro
        fields = '__all__'
