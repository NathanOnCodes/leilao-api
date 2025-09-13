from rest_framework import viewsets
from propostas.models import Propostas
from propostas.serializers import PropostaSerializer


class PropostaViewSet(viewsets.ModelViewSet):
    queryset = Propostas.objects.all()
    serializer_class = PropostaSerializer
    serializer = PropostaSerializer(queryset, many=True)
    