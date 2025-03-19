import bcrypt
import datetime
import os

from .modeloyolo import process_image
from .models import Gerente, Funcionario, Erro
from .relatorios import gerar_pdf
from .serializers import GerenteSerializer, CriarGerenteSerializer, CriarFuncionarioSerializer, FuncionarioSerializer, ErroSerializer
from base64 import decodebytes
from django.http import FileResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def gerentes(request):
    if request.method == 'GET':
        data = Gerente.objects.all()

        serializer = GerenteSerializer(data,
                                       context={'request': request},
                                       many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CriarGerenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def gerentes_modificar(request, cpf):
    try:
        gerente = Gerente.objects.get(pk=cpf)
    except Gerente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = GerenteSerializer(gerente, data=request.data,
                                       context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        gerente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def gerente_login(request):
    if request.method == 'POST':
        gerente = Gerente.objects.get(pk=request.data['cpf'])
        auth = bcrypt.checkpw(bytes(request.data['senha'], 'utf-8'),
                              bytes(gerente.senha[2:-1], 'utf-8'))
        if auth:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def funcionarios(request):
    if request.method == 'GET':
        data = Funcionario.objects.all()

        serializer = FuncionarioSerializer(data,
                                           text={'request': request},
                                           many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CriarFuncionarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def funcionarios_modificar(request, cpf):
    try:
        funcionario = Funcionario.objects.get(pk=cpf)
    except funcionario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = Funcionario.objects.filter(pk=cpf)

        serializer = FuncionarioSerializer(data,
                                           context={'request': request},
                                           many=True)

        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FuncionarioSerializer(funcionario,
                                           data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        funcionario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def funcionario_login(request):
    if request.method == 'POST':
        funcionario = Funcionario.objects.get(pk=request.data['cpf'])
        auth = bcrypt.checkpw(bytes(request.data['senha'], 'utf-8'),
                              bytes(funcionario.senha[2:-1], 'utf-8'))
        if auth:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def relatorio(request):
    if request.method == 'GET':
        erros = []
        for erro in request.data['erros']:
            err = Erro.objects.get(imagem=erro)
            e = {
                "codigo": err.imagem[:-4],
                "data": err.momento.strftime("%Y/%m/%d"),
                "hora": err.momento.strftime("%H:%M:%S.%f"),
                "linha": err.linha,
                "tipo": err.tipo,
                "imagem": os.path.join(os.path.dirname(__file__),
                                       "images",
                                       err.imagem)
            }
            erros.append(e)
        pdf_name = gerar_pdf(funcionario=request.data['funcionario'],
                             erros=erros)
        pdf_path = os.path.join(os.path.dirname(__file__), "relatorios",
                                pdf_name)
        response = FileResponse(open(pdf_path, 'rb'),
                                as_attachment=True,
                                filename=pdf_name)
        return response
    

# estrutura do json
# { 'momento': momento do erro (datetime),
#   'linha': linha do erro (int),
#   'tipo': tipo da maquininha (int),
#   'imagem': arquivo da imagem codificado para base64 (string) }

# se for pra ser sincero o codigo ta uma merda e tem que ajeitar,
# mas pra entregar daqui a algumas horas da pro gasto.
@api_view(['POST', ' GET'])
def erro(request):
    if request.method == 'POST':
        erro = Erro(momento=request.data['momento'],
                    linha=request.data['linha'],
                    tipo=request.data['tipo'])
        erro.save()
        with open(erro.imagem, "wb") as imagem:
                imagem.write(decodebytes(request.data['imagem']))
        return Response(status=status.HTTP_201_CREATED) 
    elif request.method == 'GET':
        erros = Erro.objects.all()

        response = ErroSerializer(erros, context={'request': request},
                                  many = True)
        return Response(response.data)

# estrutura do json
# { 'momento': momento do erro (string no formato %Y-%m-%d-%H-%M-%S-%f),
#   'linha': linha do erro (int),
#   'tipo': tipo da maquininha (int),
#   'image_base64': imagem codificada para base64 }
@api_view(['POST'])
def imagem(request):
    if request.method == 'POST':
        try:
            datetime_format = '%Y-%m-%d-%H-%M-%S-%f'
            momento = datetime.datetime.strptime(request.data['momento'],
                                                 datetime_format)
            image_name = (str(request.data['tipo']) + "-"
                          + str(request.data['linha']) + "_"
                          + momento.strftime("%Y-%m-%d-%H-%M-%S-%f")
                          + ".jpg")
            image_path = os.path.join(os.path.dirname(__file__),
                                      "images",
                                      image_name)
            with open(image_path, "wb") as image:
                image.write(decodebytes(request.data['image_base64']))
            errors = process_image(image_name)
            error = Erro(momento=request.data['momento'],
                         linha=request.data['linha'],
                         tipo=request.data['tipo'],
                         tela_quebrada=errors['broken_screen'],
                         carcaca_quebrada=errors['broken_shell'],
                         imagem=image_name)
            error.save()

            return Response(status=status.HTTP_201_CREATED)
        except TypeError:
            return Response(status=status.HTTP_404_NOT_FOUND)
