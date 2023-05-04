"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

# Importamos os para poder acceder a las variables de entorno
import os

# Importamos get_asgi_application para poder crear la aplicación
from django.core.asgi import get_asgi_application
#-----------------------------IMPORTAMOS LAS VISTAS-----------------------------#


#----------------------------RUTAS DE LA APLICACIÓN-----------------------------#
# Configuramos las variables de entorno
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Este archivo nos permite correr Django en tiempo real
application = get_asgi_application()
