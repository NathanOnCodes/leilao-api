from rest_framework.routers import SimpleRouter
from propostas.views import PropostaViewSet

router_propostas = SimpleRouter()

router_propostas.register(r'propostas', PropostaViewSet, basename='propostas')