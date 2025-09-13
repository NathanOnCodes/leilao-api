 
from django.contrib import admin
from django.urls import path, include
from usuarios.urls import router_usuarios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_usuarios.urls)),
]
