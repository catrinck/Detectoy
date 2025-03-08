import os

from .models import Gerente, Funcionario, ErroDetectado
from .relatorios import gerar_pdf
from .serializers import *
from base64 import decodebytes
from django.http import FileResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



import bcrypt

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

@api_view(['POST'])
def gerente_login(request):
    if request.method == 'POST':
        gerente = Gerente.objects.get(pk=request.data['cpf'])
        auth = bcrypt.checkpw(bytes(request.data['senha'], 'utf-8'), bytes(gerente.senha[2:-1], 'utf-8'))
        if auth:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def funcionarios(request):
    if request.method == 'GET':
        data = Funcionario.objects.all()

        serializer = FuncionarioSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CriarFuncionarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def funcionarios_modificar(request, cpf):
    try:
        Funcionario = Funcionario.objects.get(pk=cpf)
    except Funcionario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = Funcionario.objects.filter(pk=cpf)

        serializer = FuncionarioSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FuncionarioSerializer(Funcionario, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Funcionario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def funcionario_login(request):
    if request.method == 'POST':
        Funcionario = Funcionario.objects.get(pk=request.data['cpf'])
        auth = bcrypt.checkpw(bytes(request.data['senha'], 'utf-8'), bytes(Funcionario.senha[2:-1], 'utf-8'))
        if auth:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def relatorio(request):
    if request.method == 'GET':
        erros = []
        for erro in request.data['erros']:
            err = ErroDetectado.objects.get(imagem=erro)
            e = {
                "codigo": err.imagem[:-4],
                "data": err.momento.strftime("%Y/%m/%d"),
                "hora": err.momento.strftime("%H:%M:%S.%f"),
                "linha": ErroDetectado.linhas[err.linha],
                "tipo": ErroDetectado.tipos[err.linha],
                "imagem": os.path.join(os.path.dirname(__file__), "images", err.imagem)
            }
            erros.append(e)
        pdf_name = gerar_pdf(funcionario=request.data['funcionario'], erros=erros)
        pdf_path = os.path.join(os.path.dirname(__file__), "relatorios", pdf_name)
        response = FileResponse(open(pdf_path, 'rb'), as_attachment=True, filename=pdf_name)
        return response
    

# estrutura do json
# { 'momento': momento do erro (datetime),
#   'linha': linha do erro (int),
#   'tipo': tipo da maquininha (int),
#   'imagem': arquivo da imagem codificado para base64 (string) }

# se for pra ser sincero o codigo ta uma merda e tem que ajeitar,
# mas pra entregar daqui a algumas horas da pro gasto.
@api_view(['POST'])
def erro(request):
    if request.method == 'POST':
        erro = ErroDetectado(momento=request.data['momento'], linha=request.data['linha'], tipo=request.data['tipo'])
        erro.save()
        with open(erro.imagem, "wb") as imagem:
            imagem.write(decodebytes(request.data['imagem']))