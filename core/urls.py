 
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from usuarios.urls import router_usuarios
from propostas.urls import router_propostas

# Configurando o swagger
schema = get_schema_view(
   openapi.Info(
      title="API RESTful de Leilão",
      default_version='v1',
      description="Documentação - Siga as instruções",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_usuarios.urls)),
    path('api/', include(router_propostas.urls)),


    # URL docs
    path('docs/', schema.with_ui('swagger', cache_timeout=0), name='docs')
]
