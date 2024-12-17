from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Gerente, Usuario
from .serializers import *

@api_view(['GET', 'POST'])
def gerentes(request):
    if request.method == 'GET':
        data = Gerente.objects.all()

        serializer = GerenteSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CriarGerenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def gerentes_modificar(request, cpf):
    try:
        gerente = Gerente.objects.get(pk=cpf)
    except Gerente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'PUT':
        serializer = GerenteSerializer(gerente, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        gerente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def usuarios(request):
    if request.method == 'GET':
        data = Usuario.objects.all()

        serializer = UsuarioSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CriarUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def usuarios_modificar(request, cpf):
    try:
        usuario = Usuario.objects.get(pk=cpf)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = Usuario.objects.filter(pk=cpf)

        serializer = UsuarioSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UsuarioSerializer(usuario, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)