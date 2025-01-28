from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

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
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Serializa as ordens encontradas
    serializer = OrdemProgramacaoSerializer(ordens, many=True)
    return Response(serializer.data)
