#--------------------------IMPORTS---------------------------------#

# Importamos Images de social para poder crear las imagenes
# Importamos SocialPost de social para poder crear los posts
# Importamos SocialComment de social para poder crear los comentarios
from social.models import Image, SocialPost, SocialComment

# Importamos los modelos de la base de datos para poder usarlos en las vistas
from django.views.generic import TemplateView, View

# Importamos render para poder renderizar las paginas html
from django.shortcuts import redirect, render, get_object_or_404, redirect

# Importamos paginator para poder paginar los resultados de las busquedas
from django.core.paginator import Paginator

# Importamos UserPassesTestMixin para poder comprobar si el usuario esta logueado y creo el post
# Importamos LoginRequiredMixin para poder comprobar si el usuario esta logueado
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Importamos el formulario para crear posts y comentarios
from social.forms import SocialPostForm
#--------------------------IMPORTS---------------------------------#




#--------------------------VIEWS----------------------------------#

# Creamos la vista de la pagina principal
# Creamos la clase HomeView que hereda de la clase View
class HomeView(LoginRequiredMixin, View):

    # Creamos el metodo get para la vista de la pagina principal
    # *args significa que puede recibir un numero indefinido de argumentos
    # **kwargs significa que puede recibir un numero indefinido de argumentos con clave
    def get(self, request, *args, **kwargs):

        # Obtenemos al usuario que este logueado
        logged_in_user = request.user


        # Obtenemos todos los posts de la base de datos
        posts = SocialPost.objects.all()

        # Definimos el formulario para crear posts
        form = SocialPostForm()
        
        # Creamos el contexto para la pagina principal
        # Contexto es un diccionario que contiene los datos que se van a pasar a la pagina html
        context={

            # Definimos el formulario para crear posts
            'form': form,

            # Definimos los posts
            'posts': posts,
        }

        # Retornamos la pagina principal
        return render(request, 'pages/index.html', context)
    

    # Creamos el metodo post para la vista de la pagina principal
    # *args significa que puede recibir un numero indefinido de argumentos
    # **kwargs significa que puede recibir un numero indefinido de argumentos con clave
    def post(self, request, *args, **kwargs):

        # Obtenemos al usuario que este logueado
        logged_in_user = request.user


        # Obtenemos todos los posts de la base de datos
        posts = SocialPost.objects.all()


        # Definimos el formulario para crear posts
        # Le pasamos los datos que nos llegan por post y files
        form = SocialPostForm(request.POST, request.FILES)

        # Definimos las imagenes que nos llegan por post
        files = request.FILES.getlist('image')


        # Comprobamos si el formulario es valido
        if form.is_valid():
            # Creamos el post con los datos del formulario
            # commit=False para que no se guarde en la base de datos
            new_post = form.save(commit=False)

            # Definimos el usuario que creo el post como el usuario que esta logueado
            new_post.author = logged_in_user

            # Guardamos el post en la base de datos
            new_post.save()

            # Recorremos las imagenes que nos llegan por post
            for f in files:

                # Definimos image como la imagen que nos llega por post
                img = Image(image=f)

                # Guardamos la imagen en la base de datos
                img.save()

                # Añadimos la imagen al post
                new_post.image.add(img)

            # Guardamos el post en la base de datos
            new_post.save()
            
        
        # Creamos el contexto para la pagina principal
        # Contexto es un diccionario que contiene los datos que se van a pasar a la pagina html
        context={

            # Definimos el formulario para crear posts
            'form': form,

            # Definimos los posts
            'posts': posts,
        }

        # Retornamos la pagina principal
        return render(request, 'pages/index.html', context)
#-------------------------END VIEWS-------------------------------#