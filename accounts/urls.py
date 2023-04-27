# Usaremos este documento para extender las urls de la aplicación accounts

# Importamos las librerías necesarias

# Importamos path para poder usar las rutas
from django.urls import path
#------------------------------IMPORT BOOKSTORES--------------------------------


# Definimos la app_name para poder usarla en las plantillas de la aplicación
app_name = 'accounts'


# Creamos las urls de la aplicación accounts
urlpatterns = [

    # Cremos la ruta del perfil del usuario
    path('users/<username>', name='profile'),

]