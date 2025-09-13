 
from django.contrib import admin
from django.urls import path, include
from usuarios.urls import router_usuarios
from propostas.urls import router_propostas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_usuarios.urls)),
    path('api/', include(router_propostas.urls)),
]
