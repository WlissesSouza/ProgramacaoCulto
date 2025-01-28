from rest_framework import serializers
from .models import OrdemProgramacao


class OrdemProgramacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemProgramacao
        fields = '__all__'
