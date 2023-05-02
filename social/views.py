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
#------------------------------IMPORT MODELS-----------------------------



#------------------------------VIEWS-------------------------------------

# Creamos una vista para para poder acceder a los posts
class PostDetailView(LoginRequiredMixin, View):

    # Utilizamos get para poder acceder a los posts mediante la url
    def get(self, request, *args, **kwargs):

        # Retornamos la plantilla de detalle de los posts
        return render(request, 'pages/social/detail.html', {

            # Obtenemos el post que queremos ver
            'post': SocialPost.objects.get(pk=pk),

            # Obtenemos los comentarios del post que queremos ver
            'comments': SocialComment.objects.filter(post=pk)
        })




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

        # Obtenemos el id del post que queremos editar
        pk = self.get_object()

        # Redireccionamos a la url de detalle del post
        # Usamos kwargs para pasarle el id del post que queremos editar
        # kwargs nos sirve para pasar los elementos que tiene un objeto
        return reverse_lazy('social:post_detail', kwargs={'pk': pk})
    

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