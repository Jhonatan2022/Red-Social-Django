# Importamos LoginRequiredMixin para que solo los usuarios logueados puedan acceder a las vistas
# Importamos UserPassesTestMixin para que solo los usuarios que hayan creado el post puedan editarlos
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Importamos render para poder renderizar las vistas
from django.shortcuts import render

# Importamos reverse_lazy para poder redireccionar a una url
from django.urls.base import reverse_lazy

# Importamos View para poder crear las vistas
from django.views.generic.base import View

# Importamos SocialPost para poder editar los posts
# Importamos SocialComment para poder editar los comentarios
from .models import SocialPost, SocialComment

# Importamos UpdateView para poder editar los posts
# Importamos DeleteView para poder eliminar los posts
from django.views.generic.edit import UpdateView, DeleteView

# Importamos httprresponse para poder redireccionar a una url
from django.http.response import HttpResponseRedirect, HttpResponse
#------------------------------IMPORT MODELS-----------------------------



#------------------------------VIEWS-------------------------------------

# Creamos una vista para para poder acceder a los posts
class PostDetailView(LoginRequiredMixin, View):

    # Utilizamos get para poder acceder a los posts mediante la url
    # Jalamos el pk para poder acceder a los posts mediante la url
    def get(self, request, pk, *args, **kwargs):

        # Llamamos al modelo SocialPost para poder acceder a los posts especificos
        # Usamos pk para poder acceder a los posts mediante la url
        post = SocialPost.objects.get(pk=pk)

        # Creamos el contexto
        context = {

            # Pasamos el post para poder acceder a los posts especificos
            'post': post,
        }

        # Retornamos la plantilla de detalle de los posts
        return render(request, 'pages/social/detail.html', context)
    
    

    # Utilizamos post para poder acceder a los posts mediante la url
    # Jalamos el pk para poder acceder a los posts mediante la url
    def post(self, request, pk, *args, **kwargs):

        # Llamamos al modelo SocialPost para poder acceder a los posts especificos
        # Usamos pk para poder acceder a los posts mediante la url
        post = SocialPost.objects.get(pk=pk)

        # Creamos el contexto
        context = {

            # Pasamos el post para poder acceder a los posts especificos
            'post': post,
        }

        # Retornamos la plantilla de detalle de los posts
        return render(request, 'pages/social/detail.html', context)



# Creamos una vista para poder editar los posts
class PostEditView(LoginRequiredMixin, UserPassesTestMixin , UpdateView):

    # Llamamos al modelo SocialPost para poder editar los posts
    model = SocialPost

    # Indicamos los campos que queremos editar
    fields = ['body']

    # Indicamos la plantilla que queremos usar
    template_name = 'pages/social/edit.html'


    # Indicamos el nombre de la url a la que queremos redireccionar
    def get_success_url(self):

        # Obtenemos el id del post que queremos editar por medio de kwargs
        pk = self.kwargs['pk']

        # Redireccionamos a la url de detalle del post
        # Usamos kwargs para pasarle el id del post que queremos editar
        # kwargs nos sirve para pasar los elementos que tiene un objeto
        return reverse_lazy('social:post-detail', kwargs={'pk': pk})
    


    # Indicamos que solo los usuarios que hayan creado el post puedan editarlos
    def test_func(self):

        # Obtenemos el post que queremos editar
        post = self.get_object()

        # Comprobamos si el usuario logueado es el creador del post
        return self.request.user == post.author



# Creamos una vista para poder eliminar los posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin , DeleteView):

    # Llamamos al modelo SocialPost para poder eliminar los posts
    model = SocialPost

    # Indicamos la plantilla que queremos usar
    template_name = 'pages/social/delete.html'


    # Indicamos el nombre de la url a la que queremos redireccionar
    # Redireccionamos a la url de inicio
    success_url = reverse_lazy('home')
    

    # Indicamos que solo los usuarios que hayan creado el post puedan eliminarlos
    def test_func(self):

        # Obtenemos el post que queremos eliminar
        post = self.get_object()

        # Comprobamos si el usuario logueado es el creador del post
        return self.request.user == post.author
    


# Creamos una vista para poder dar like a los posts
class AddLike(LoginRequiredMixin, View):

    # Utilizamos post para poder dar like a los posts
    # Jalamos el pk para poder dar like a los posts mediante la url
    def post(self, request, pk, *args, **kwargs):

        # Llamamos al modelo SocialPost para poder dar like a los posts
        # Usamos pk para poder dar like a los posts mediante la url
        post = SocialPost.objects.get(pk=pk)



        # Iniciamos diciendo que dislike es falso
        is_dislike = False

        # Cremos un ciclo for para poder recorrer los likes
        for dilike in post.dislikes.all():

            # Comprobamos si el usuario logueado esta en los dislikes
            if dilike == request.user:

                # Si el usuario logueado esta en los dislikes, entonces dislike es verdadero
                is_dislike = True
                # Rompemos el ciclo
                break

        # Si dislike es verdadero, entonces eliminamos el dislike
        if is_dislike:

            # Eliminamos el dislike
            post.dislikes.remove(request.user)


        # Iniciamos diciendo que like es falso
        is_like = False

        # Cremos un ciclo for para poder recorrer los likes
        for like in post.likes.all():

            # Comprobamos si el usuario logueado esta en los likes
            if like == request.user:

                # Si el usuario logueado esta en los likes, entonces like es verdadero
                is_like = True
                # Rompemos el ciclo
                break

        # Si like es falso, entonces agregamos el like
        if not is_like:

            # Agregamos el like
            post.likes.add(request.user)

        # Si like es verdadero, entonces eliminamos el like
        if is_like:

            # Eliminamos el like
            post.likes.remove(request.user)


        # Redireccionamos a la url de inicio
        next = request.POST.get('next', '/')

        # Retornamos la redireccion
        return HttpResponseRedirect(next)




# Creamos una vista para poder dar dislike a los posts
class AddDislike(LoginRequiredMixin, View):

    # Utilizamos post para poder dar dislike a los posts
    # Jalamos el pk para poder dar dislike a los posts mediante la url
    def post(self, request, pk, *args, **kwargs):

        # Llamamos al modelo SocialPost para poder dar dislike a los posts
        # Usamos pk para poder dar dislike a los posts mediante la url
        post = SocialPost.objects.get(pk=pk)



        # Iniciamos diciendo que like es falso
        is_like = False

        # Cremos un ciclo for para poder recorrer los likes
        for like in post.likes.all():

            # Comprobamos si el usuario logueado esta en los likes
            if like == request.user:

                # Si el usuario logueado esta en los likes, entonces like es verdadero
                is_like = True
                # Rompemos el ciclo
                break

        # Si like es verdadero, entonces eliminamos el like
        if is_like:

            # Eliminamos el like
            post.likes.remove(request.user)


        # Iniciamos diciendo que dislike es falso
        is_dislike = False

        # Cremos un ciclo for para poder recorrer los dislikes
        for dilike in post.dislikes.all():

            # Comprobamos si el usuario logueado esta en los dislikes
            if dilike == request.user:

                # Si el usuario logueado esta en los dislikes, entonces dislike es verdadero
                is_dislike = True
                # Rompemos el ciclo
                break


        # Si dislike es falso, entonces agregamos el dislike
        if not is_dislike:

            # Agregamos el dislike
            post.dislikes.add(request.user)


        # Si dislike es verdadero, entonces eliminamos el dislike
        if is_dislike:

            # Eliminamos el dislike
            post.dislikes.remove(request.user)


        # Redireccionamos a la url de inicio
        next = request.POST.get('next', '/')

        # Retornamos la redireccion
        return HttpResponseRedirect(next)