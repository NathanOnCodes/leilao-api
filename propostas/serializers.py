from rest_framework import serializers
from propostas.models import Propostas


class PropostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propostas
        fields = '__all__'