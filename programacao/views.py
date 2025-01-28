from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import OrdemProgramacao
from .serealizers import OrdemProgramacaoSerializer

import json


@api_view(['GET'])
def get_programacao(request):
    if request.method == 'GET':
        programacao = OrdemProgramacao.objects.all()

        serializer = OrdemProgramacaoSerializer(programacao, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_by_programacao(request, programacao):
    try:
        # Filtra todas as ordens de programação que pertencem ao número de programação fornecido
        ordens = OrdemProgramacao.objects.filter(programacao__id=programacao)

        # Se não houver ordens, retorna uma mensagem apropriada
        if not ordens.exists():
            return Response({'error': 'Nenhuma ordem encontrada para esta programação.'},
                            status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': 'Nenhuma ordem encontrada para esta programação.'}, status=status.HTTP_400_BAD_REQUEST)

    # Serializa as ordens encontradas
    serializer = OrdemProgramacaoSerializer(ordens, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def programacao_manage(request):
    if request.method == 'GET':
        try:
            if request.GET['cod']:
                cod = request.GET['cod']
                try:
                    lista_programacao = OrdemProgramacao.objects.filter(programacao__id=cod)
                    if len(lista_programacao) == 0:
                        return Response(status=status.HTTP_404_NOT_FOUND)
                except Exception as e:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serealizador = OrdemProgramacaoSerializer(lista_programacao, many=True)
                return Response({'programacao': serealizador.data})
            else:
                Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Nenhuma ordem encontrada para esta programação.'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        novo_item = request.data
        try:
            serializador = OrdemProgramacaoSerializer(data=novo_item)
            if serializador.is_valid():
                serializador.save()
                return Response({serializador.data}, status.HTTP_201_CREATED)
            else:
                return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        cod = request.GET['cod']
        try:
            update_programacao = OrdemProgramacao.objects.get(pk=cod)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serealizador = OrdemProgramacaoSerializer(update_programacao, data=request.data)
        if serealizador.is_valid():
            serealizador.save()
            return Response({serealizador.data}, status.HTTP_202_ACCEPTED)
        return Response({'programacao': serealizador.data})
