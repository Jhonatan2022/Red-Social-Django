# Usaremos este documento para extender las urls de la aplicación accounts

# Importamos las librerías necesarias

# Importamos path para poder usar las rutas
from django.urls import path

# Importamos las vistas de la aplicación
from .views import ProfileView
#------------------------------IMPORT BOOKSTORES--------------------------------




#------------------------------IMPORT VIEWS--------------------------------
# Definimos la app_name para poder usarla en las plantillas de la aplicación
app_name = "accounts"


# Creamos las urls de la aplicación accounts
urlpatterns = [

    # Cremos la ruta del perfil del usuario
    # as_view(): Es una función que nos permite convertir una clase en una vista
    path('<username>/', ProfileView.as_view(), name='profile'),

]