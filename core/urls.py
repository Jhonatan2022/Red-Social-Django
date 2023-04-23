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

# Importamos path para crear las rutas, include para incluir otras rutas
from django.urls import path, include

# Importamos settings para poder acceder a las variables de configuración
from django.conf import settings

# Importamos static para poder acceder a las variables de configuración
from django.conf.urls.static import static

# Importamos la vista de la pagina principal que creamos en views.py
from .views import HomeView
#-----------------------------IMPORTAMOS LAS LIBRERIAS-------------------------#



#----------------------------RUTAS DE LA APLICACIÓN-----------------------------#
# Creamos las rutas
urlpatterns = [

    # Ruta para acceder al panel de administración
    path('admin/', admin.site.urls),

    # Coloca la ruta de la aplicación que creaste en la carpeta apps
    path('accounts/', include('allauth.urls')),

    # Ruta para acceder a la pagina principal
    # Al ser una vista de clase, colocamos as_view() para que se ejecute el metodo get
    path('', HomeView.as_view(), name='home'),
]
#----------------------------RUTAS DE LA APLICACIÓN-----------------------------#


if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)