# Usaremos este documento para extender las urls de la aplicación accounts

# Importamos las librerías necesarias

# Importamos path para poder usar las rutas
from django.urls import path

# Importamos las vistas de la aplicación
from .views import UserProfileView, EditProfile, AddFollower, RemoveFollower, ListFollowers
#------------------------------IMPORT BOOKSTORES--------------------------





#------------------------------IMPORT VIEWS-------------------------------
# Definimos la app_name para poder usarla en las plantillas de la aplicación
app_name = "accounts"




#------------------------------URLS--------------------------------
# Creamos las urls de la aplicación accounts
urlpatterns = [


    # Cremos la ruta del perfil del usuario
    # as_view(): Es una función que nos permite convertir una clase en una vista
    path('<username>/', UserProfileView, name='profile'),


    # Cremos la ruta para editar el perfil del usuario
    # as_view(): Es una función que nos permite convertir una clase en una vista
    path('profile/edit', EditProfile, name='edit'),


    # Cremos la ruta para seguir a un usuario
    # as_view(): Es una función que nos permite convertir una clase en una vista
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),


    # Cremos la ruta para dejar de seguir a un usuario
    # as_view(): Es una función que nos permite convertir una clase en una vista
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),


    # Cremos la ruta para mostrar los seguidores de un usuario
    # as_view(): Es una función que nos permite convertir una clase en una vista
    path('profile/<int:pk>/followers/', ListFollowers.as_view(), name='followers-list'),
]