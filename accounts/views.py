#--------------------------IMPORTS---------------------------------#
# Importamos los modelos de la base de datos para poder usarlos en las vistas
from django.views.generic import View

# Importamos render para poder renderizar las paginas html
from django.shortcuts import render, get_object_or_404

# Importamos Profile para poder usar el modelo de perfil
from accounts.models import Profile

# Importamos User para poder usar el modelo de usuario
from django.contrib.auth import get_user_model
#--------------------------IMPORTS---------------------------------#

# Definimos el modelo User como get_user_model()
User = get_user_model()




#----------------------------VIEWS---------------------------------#
# Creamos una vista para el perfil del usuario
class ProfileView(View):

    # Creamos una funcion para obtener el contexto
    # request: Es la solicitud que se hace al servidor
    # args: Es una lista de argumentos posicionales que se pasan a la vista
    # kwargs: Es un diccionario de argumentos de palabras clave que se pasan a la vista
    # self: Es una referencia a la instancia actual de la clase
    def get(self, request, username, *args, **kwargs):

        # Obtenemos el contexto del usuario logueado
        user = get_object_or_404(User, username=username)

        # Determinamos si el perfil es del usuario logueado o de otro usuario
        profile = Profile.objects.get(user=user)

        # Obtenemos el contexto
        context ={
            
            # Obtenemos el usuario logueado
            'user':user,

            # Obtenemos el perfil del usuario
            'profile':profile
            }   
        

        # Retornamo y renderizamos el perfil del usuario
        return render(request, 'users/detail.html', context)