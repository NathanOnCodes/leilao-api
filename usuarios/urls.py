from usuarios.views import (
    UsuariosViewSet,
)
from rest_framework.routers import SimpleRouter


router_usuarios = SimpleRouter()

router_usuarios.register(
    r'usuarios',
    UsuariosViewSet,
    basename='usuarios'
)
