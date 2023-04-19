"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Importamos admin para poder acceder al panel de administración
from django.contrib import admin

# Importamos path para crear las rutas
from django.urls import path
#-----------------------------IMPORTAMOS LAS LIBRERIAS-------------------------#



#----------------------------RUTAS DE LA APLICACIÓN-----------------------------#
# Creamos las rutas
urlpatterns = [

    # Ruta para acceder al panel de administración
    path('admin/', admin.site.urls),
]
