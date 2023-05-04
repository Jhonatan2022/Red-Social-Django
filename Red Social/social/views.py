# Importamos SocialCommentForm para poder crear los comentarios
from social.forms import SocialCommentForm

# Importamos LoginRequiredMixin para que solo los usuarios logueados puedan acceder a las vistas
# Importamos UserPassesTestMixin para que solo los usuarios que hayan creado el post puedan editarlos
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Importamos render para poder renderizar las vistas
from django.shortcuts import render, redirect

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

        # Creamos la posibilidad de crear un comentario
        form = SocialCommentForm()

        # Cargamos todos los comentarios del post
        # Usamos order_by para ordenar los comentarios de mas reciente a mas antiguo
        # Usamos -created_on para ordenar los comentarios de mas reciente a mas antiguo
        comments = SocialComment.objects.filter(post=post).order_by('-created_on')

        # Creamos el contexto
        context = {

            # Pasamos el post para poder acceder a los posts especificos
            'post': post,

            # Pasamos el formulario para poder crear comentarios
            'form': form,

            # Pasamos los comentarios para poder acceder a los comentarios especificos
            'comments': comments
        }

        # Retornamos la plantilla de detalle de los posts
        return render(request, 'pages/social/detail.html', context)
    
    

    # Utilizamos post para poder acceder a los posts mediante la url
    # Jalamos el pk para poder acceder a los posts mediante la url
    def post(self, request, pk, *args, **kwargs):

        # Llamamos al modelo SocialPost para poder acceder a los posts especificos
        # Usamos pk para poder acceder a los posts mediante la url
        post = SocialPost.objects.get(pk=pk)

        # Creamos la posibilidad de crear un comentario
        form = SocialCommentForm(request.POST)

        # Cargamos todos los comentarios del post
        # Usamos order_by para ordenar los comentarios de mas reciente a mas antiguo
        # Usamos -created_on para ordenar los comentarios de mas reciente a mas antiguo
        comments = SocialComment.objects.filter(post=post).order_by('-created_on')

        # Validamos el formulario
        if form.is_valid():

            # Guardamos el comentario pero no lo subimos a la base de datos
            new_comment = form.save(commit=False)

            # Guardamos el autor del comentario
            new_comment.author = request.user

            # Guardamos el post al que pertenece el comentario
            new_comment.post = post

            # Subimos el comentario a la base de datos
            new_comment.save()

            # Redireccionamos a la url de detalle del post
            # Usamos kwargs para pasarle el id del post que queremos editar
            return HttpResponseRedirect(reverse_lazy('social:post-detail', kwargs={'pk': pk}))

        # Creamos el contexto
        context = {

            # Pasamos el post para poder acceder a los posts especificos
            'post': post,

            # Pasamos el formulario para poder crear comentarios
            'form': form,

            # Pasamos los comentarios para poder acceder a los comentarios especificos
            'comments': comments
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
    



# Creamos una vista para poder dar like a los comentarios
class AddCommentLike(LoginRequiredMixin, View):

    # Utilizamos post para poder dar like a los comentarios
    # Jalamos el pk para poder dar like a los comentarios mediante la url
    def post(self, request, pk, *args, **kwargs):

        # Llamamos al modelo Comment para poder dar like a los comentarios
        # Usamos pk para poder dar like a los comentarios mediante la url
        comment = SocialComment.objects.get(pk=pk)



        # Iniciamos diciendo que dislike es falso
        is_dislike = False

        # Cremos un ciclo for para poder recorrer los likes
        for dilike in comment.dislikes.all():

            # Comprobamos si el usuario logueado esta en los dislikes
            if dilike == request.user:

                # Si el usuario logueado esta en los dislikes, entonces dislike es verdadero
                is_dislike = True
                # Rompemos el ciclo
                break

        # Si dislike es verdadero, entonces eliminamos el dislike
        if is_dislike:

            # Eliminamos el dislike
            comment.dislikes.remove(request.user)


        # Iniciamos diciendo que like es falso
        is_like = False

        # Cremos un ciclo for para poder recorrer los likes
        for like in comment.likes.all():

            # Comprobamos si el usuario logueado esta en los likes
            if like == request.user:

                # Si el usuario logueado esta en los likes, entonces like es verdadero
                is_like = True
                # Rompemos el ciclo
                break

        # Si like es falso, entonces agregamos el like
        if not is_like:

            # Agregamos el like
            comment.likes.add(request.user)

        # Si like es verdadero, entonces eliminamos el like
        if is_like:

            # Eliminamos el like
            comment.likes.remove(request.user)


        # Redireccionamos a la url de inicio
        next = request.POST.get('next', '/')

        # Retornamos la redireccion
        return HttpResponseRedirect(next)




# Creamos una vista para poder dar dislike a los comentarios
class AddCommentDislike(LoginRequiredMixin, View):

    # Utilizamos post para poder dar dislike a los comentarios
    # Jalamos el pk para poder dar dislike a los comentarios mediante la url
    def post(self, request, pk, *args, **kwargs):

        # Llamamos al modelo Comment para poder dar dislike a los comentarios
        # Usamos pk para poder dar dislike a los comentarios mediante la url
        comment = SocialComment.objects.get(pk=pk)



        # Iniciamos diciendo que like es falso
        is_like = False

        # Cremos un ciclo for para poder recorrer los likes
        for like in comment.likes.all():

            # Comprobamos si el usuario logueado esta en los likes
            if like == request.user:

                # Si el usuario logueado esta en los likes, entonces like es verdadero
                is_like = True
                # Rompemos el ciclo
                break

        # Si like es verdadero, entonces eliminamos el like
        if is_like:

            # Eliminamos el like
            comment.likes.remove(request.user)


        # Iniciamos diciendo que dislike es falso
        is_dislike = False

        # Cremos un ciclo for para poder recorrer los dislikes
        for dilike in comment.dislikes.all():

            # Comprobamos si el usuario logueado esta en los dislikes
            if dilike == request.user:

                # Si el usuario logueado esta en los dislikes, entonces dislike es verdadero
                is_dislike = True
                # Rompemos el ciclo
                break


        # Si dislike es falso, entonces agregamos el dislike
        if not is_dislike:

            # Agregamos el dislike
            comment.dislikes.add(request.user)


        # Si dislike es verdadero, entonces eliminamos el dislike
        if is_dislike:

            # Eliminamos el dislike
            comment.dislikes.remove(request.user)


        # Redireccionamos a la url de inicio
        next = request.POST.get('next', '/')

        # Retornamos la redireccion
        return HttpResponseRedirect(next)
    



# Creamos una vista para poder responder comentarios
class CommentReplyView(LoginRequiredMixin, View):

    # Utilizamos post para poder responder comentarios
    # Jalamos el pk para poder responder comentarios mediante la url
    def post(self, request, post_pk, pk, *args, **kwargs):
        
        # Llamamos al modelo Comment para poder responder comentarios
        # Usamos pk para poder responder comentarios mediante la url
        post = SocialPost.objects.get(pk=post_pk)

        # Obtenemos el comentario padre mediante el pk
        parent_comment = SocialComment.objects.get(pk=pk)

        # Llamamos al formulario de responder comentarios
        form = SocialCommentForm(request.POST)


        # Si el formulario es valido
        if form.is_valid():

            # Guardamos el formulario
            new_comment = form.save(commit=False)

            # Guardamos el usuario logueado
            new_comment.author = request.user

            # Guardamos el post
            new_comment.post = post

            # Guardamos el comentario padre
            new_comment.parent = parent_comment

            # Guardamos el formulario
            new_comment.save()
            

            # Retornamos y redireccionamos al post detail
            return redirect('social:post-detail', pk=post_pk)




# Creamos una vista para poder eliminar comentarios
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    # Llamamos al modelo Comment para poder eliminar comentarios
    model = SocialComment

    # Llamamos al template de eliminar comentarios
    template_name = 'pages/social/comment_delete.html'

    # Indicamos el nombre de la url a la que queremos redireccionar
    def get_success_url(self):

        # Obtenemos el id del post que queremos editar por medio de kwargs
        pk = self.kwargs['post_pk']

        # Redireccionamos a la url de detalle del post
        # Usamos kwargs para pasarle el id del post que queremos editar
        # kwargs nos sirve para pasar los elementos que tiene un objeto
        return reverse_lazy('social:post-detail', kwargs={'pk': pk})
    

    # Creamos una funcion para poder comprobar si el usuario logueado es el autor del post
    def test_func(self):

        # Obtenemos el id del post que queremos editar por medio de kwargs
        post = self.get_object()

        # Retornamos si el usuario logueado es el autor del post
        return self.request.user == post.author
    



# Creamos la vista para poder editar comentarios
class CommentEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    # Llamamos al modelo Comment para poder editar comentarios
    model = SocialComment

    # Indicamos los campos que vamos a editar
    fields = ['comment']

    # Llamamos al template de editar comentarios
    template_name = 'pages/social/comment_edit.html'

    # Indicamos el nombre de la url a la que queremos redireccionar
    def get_success_url(self):

        # Obtenemos el id del post que queremos editar por medio de kwargs
        pk = self.kwargs['post_pk']

        # Redireccionamos a la url de detalle del post
        # Usamos kwargs para pasarle el id del post que queremos editar
        # kwargs nos sirve para pasar los elementos que tiene un objeto
        return reverse_lazy('social:post-detail', kwargs={'pk': pk})
    

    # Creamos una funcion para poder comprobar si el usuario logueado es el autor del post
    def test_func(self):

        # Obtenemos el id del post que queremos editar por medio de kwargs
        post = self.get_object()

        # Retornamos si el usuario logueado es el autor del post
        return self.request.user == post.author