from rest_framework import viewsets
from usuarios.models import Usuarios
from usuarios.serializers import UsuarioSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuarios.objects.all()
    serializer = UsuarioSerializer(queryset, many=True)