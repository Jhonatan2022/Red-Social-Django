#--------------------------IMPORTS---------------------------------#
# Importamos los modelos de la base de datos para poder usarlos en las vistas
from django.views.generic import TemplateView, View

# Importamos render para poder renderizar las paginas html
from django.shortcuts import redirect, render, get_object_or_404, redirect

# Importamos paginator para poder paginar los resultados de las busquedas
from django.core.paginator import Paginator

# Importamos render para poder renderizar las paginas html
from django.shortcuts import render
#--------------------------IMPORTS---------------------------------#




#----------------------------VIEWS---------------------------------#

# Creamos una vista para el perfil del usuario
class ProfileView(TemplateView):

    # Definimos el template_name
    template_name = 'accounts/profile.html'

    # Definimos el metodo get
    def get(self, request, username):

        # Obtenemos el usuario
        user = get_object_or_404(User, username=username)

        # Obtenemos los libros del u