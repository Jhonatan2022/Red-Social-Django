#--------------------------IMPORTS---------------------------------#

# Importamos los modelos de la base de datos para poder usarlos en las vistas
from django.views.generic import TemplateView, View

# Importamos render para poder renderizar las paginas html
from django.shortcuts import redirect, render, get_object_or_404, redirect

# Importamos paginator para poder paginar los resultados de las busquedas
from django.core.paginator import Paginator
#--------------------------IMPORTS---------------------------------#



#--------------------------VIEWS----------------------------------#

# Creamos la vista de la pagina principal
# Creamos la clase HomeView que hereda de la clase View
class HomeView(View):

    # Creamos el metodo get para la vista de la pagina principal
    # *args significa que puede recibir un numero indefinido de argumentos
    # **kwargs significa que puede recibir un numero indefinido de argumentos con clave
    def get(self, request, *args, **kwargs):
        
        # Creamos el contexto para la pagina principal
        # Contexto es un diccionario que contiene los datos que se van a pasar a la pagina html
        context={

        }

        # Retornamos la pagina principal
        return render(request, 'pages/index.html', context)