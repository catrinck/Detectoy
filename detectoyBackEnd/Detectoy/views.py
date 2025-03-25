import bcrypt
import datetime
import os

from .modeloyolo import process_image
from .models import Gerente, Funcionario, Erro
from .relatorios import gerar_pdf
from .serializers import GerenteSerializer, CriarGerenteSerializer, CriarFuncionarioSerializer, FuncionarioSerializer, ErroSerializer
from base64 import b64decode
from django.http import FileResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



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
    try:
        gerente = Gerente.objects.get(pk=request.data['cpf'])
        auth = bcrypt.checkpw(bytes(request.data['senha'], 'utf-8'),
                              bytes(gerente.senha[2:-1], 'utf-8'))
        if auth:
            # Gerar um token JWT
            refresh = RefreshToken.for_user(gerente)
            return Response({
                "refresh": str(refresh),
                "token": str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        return Response({"error": "Credenciais inválidas"}, status=status.HTTP_400_BAD_REQUEST)
    except Gerente.DoesNotExist:
            return Response({"error": "Gerente não encontrado"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def funcionarios(request):
    if request.method == 'GET':
        data = Funcionario.objects.all()

        serializer = FuncionarioSerializer(data,
                                           context={'request': request},
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
# { 'momento': momento do erro (string no formato %Y-%m-%d-%H-%M-%S-%f),
#   'linha': linha do erro (int),
#   'tipo': tipo da maquininha (int),
#   'image_base64': imagem codificada para base64 }
@api_view(['POST', 'GET'])
def erro(request):
    if request.method == 'POST':
        try:
            print("Json:\n-----")
            print("momento: ", request.data['momento'])
            print("linha: ", request.data['linha'])
            print("tipo: ", request.data['tipo'])
            print("-----\nCasting momento to datetime...")
            datetime_format = '%Y-%m-%d-%H-%M-%S-%f'
            momento = datetime.datetime.strptime(request.data['momento'],
                                                 datetime_format)
            print("Done")
            print("Setting image name...")
            image_name = (str(request.data['tipo']) + "-"
                          + str(request.data['linha']) + "_"
                          + momento.strftime("%Y-%m-%d-%H-%M-%S-%f")
                          + ".jpg")
            print("Done")
            print("Setting image path...")
            image_path = os.path.join(os.path.dirname(__file__),
                                      "images",
                                      image_name)
            print("Done")
            print("Openning image...")
            with open(image_path, "wb") as image:
                print("Done")
                print("Writing base64 to image...")
                image.write(b64decode(request.data['image_base64']))
                print("Done")
                print("Closing image...")
                image.close()
                print("Done")
            print("Processing image...")
            errors = process_image(image_name)
            print("Done")
            print("Creating object Erro...")
            error = Erro(momento=momento,
                         linha=request.data['linha'],
                         tipo=request.data['tipo'],
                         tela_quebrada=errors['broken_screen'],
                         carcaca_quebrada=errors['broken_shell'],
                         imagem=image_name)
            print("Done")
            print("Saving object...")
            error.save()
            print("Done")

            return Response(status=status.HTTP_201_CREATED)
        except TypeError:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'GET':
        erros = Erro.objects.all()

        response = ErroSerializer(erros, context={'request': request},
                                  many = True)
        return Response(response.data)
