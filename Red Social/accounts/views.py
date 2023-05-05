#--------------------------IMPORTS---------------------------------#
# Importamos los modelos de la base de datos para poder usarlos en las vistas
from django.views.generic import View

# Importamos el formulario para editar el perfil
from accounts.forms import EditProfileForm

# Importamos render para poder renderizar las paginas html
# redirect para poder redireccionar a otra pagina
# get_object_or_404 para poder obtener un objeto o devolver un error 404
# render para poder renderizar las paginas html
from django.shortcuts import redirect, render, get_object_or_404

# Importamos Profile para poder usar el modelo de perfil
from accounts.models import Profile

# Importamos User para poder usar el modelo de usuario
from django.contrib.auth import get_user_model

# Importamos login_required para poder usar el decorador de login
from django.contrib.auth.decorators import login_required

# Importamos LoginRequiredMixin para poder usar el mixin de login
from django.contrib.auth.mixins import LoginRequiredMixin

# Importamos messages para poder mostrar mensajes en el html de la pagina
from django.contrib import messages

# Importamos loader para poder cargar los templates
from django.template import loader

# Importamos HttpResponse para poder devolver una respuesta
from django.http import HttpResponse
#--------------------------IMPORTS---------------------------------#




# Definimos el modelo User como get_user_model()
User = get_user_model()




#----------------------------VIEWS---------------------------------#
# Creamos una vista para el perfil del usuario
@login_required
def UserProfileView(request, username):

        # Obtenemos el contexto del usuario logueado
        user = get_object_or_404(User, username=username)

        # Determinamos si el perfil es del usuario logueado o de otro usuario
        profile = Profile.objects.get(user=user)

        # Obtenemos los seguidores del usuario
        followers = profile.followers.all()


        # Si el numero de seguidores igual a 0
        if len(followers) == 0:

            # Pasamos False a la variable is_following
            is_following = False


        # Si estamos siguiendo a un usuario y estamos en la lista de seguidores
        for follower in followers:

            # Si el usuario logueado esta en la lista de seguidores
            if follower == request.user:

                # Pasamos True a la variable is_following
                is_following = True
                # Rompemos el ciclo
                break

            # Si el usuario logueado no esta en la lista de seguidores
            else:

                # Pasamos False a la variable is_following
                is_following = False


        # Hacemos un conteo de los seguidores del usuario
        # Usamos len() para contar los seguidores del usuario
        # Len es una funcion que nos permite contar los elementos de una lista
        number_of_followers = len(followers)


        # Cargamos el template del perfil del usuario
        template = loader.get_template('users/detail.html')


        # Obtenemos el contexto
        context ={

            # Obtenemos el perfil del usuario
            'profile':profile,

            # Obtenemos el numero de seguidores del usuario
            'number_of_followers':number_of_followers,

            # Obtenemos si estamos siguiendo al usuario
            'is_following':is_following,
            }   
        

        # Retornamo 
        return HttpResponse(template.render(context, request))
    



# Creamos una vista para editar el perfil del usuario
# Login_required: Es un decorador que nos permite restringir el acceso a una vista
@login_required
def EditProfile(request):

    # Identificamos que el usuario logueado es el mismo que el perfil que se va a editar
    user = request.user.id

    # Obtenemos el perfil del usuario
    profile = Profile.objects.get(user__id=user)

    # Obtenemos la informacion del usuario logueado
    user_basic_info = User.objects.get(id=user) 


    # Definimos el formulario para editar el perfil
    if request.method == 'POST':

        # Obtenemos el formulario para editar el perfil
        # request.POST: Es un diccionario que contiene todos los datos enviados por el usuario
        # request.FILES: Es un diccionario que contiene todos los archivos enviados por el usuario
        # instance: Es una instancia del modelo que se va a editar
        form = EditProfileForm(request.POST, request.FILES, instance=profile)

        # Verificamos que el formulario sea valido
        if form.is_valid():

            # Hacemos referencia a user__info para poder editar los campos del usuario
            # Cleaned_data: Es un diccionario que contiene los datos validos del formulario
            user_basic_info = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')


            # Pasaremos a editar el perfil del usuario
            # hacemos referencia a la imagen de perfil del usuario
            profile.picture = form.cleaned_data.get('picture')

            # hacemos referencia a la imagen de banner del usuario
            profile.banner = form.cleaned_data.get('banner')

            # hacemos referencia a la ubicacion del usuario
            profile.location = form.cleaned_data.get('location')

            # hacemos referencia a la sitio web del usuario
            profile.website = form.cleaned_data.get('website')

            # hacemos referencia a la fecha de nacimiento del usuario
            profile.birthday = form.cleaned_data.get('birthday')

            # hacemos referencia a la biografia del usuario
            profile.biography = form.cleaned_data.get('biography') 

            # Guardamos los cambios del perfil
            profile.save()

            # Guardamos los cambios
            # Guardamos los cambios del usuario
            user_basic_info.save()

            # Redireccionamos al perfil del usuario
            return redirect('users:profile', username = request.user.username)
        
    # Si el metodo es GET
    else:

        # Obtenemos el formulario para editar el perfil
        form = EditProfileForm(instance=profile)


    # Obtenemos el contexto
    context = {

        # Obtenemos el formulario para editar el perfil
        'form':form,
    }

    # Retornamos y renderizamos el formulario para editar el perfil
    return render(request, 'users/edit.html', context)




# Creamos una vista para seguir a un usuario o dejar de seguirlo
class AddFollower(LoginRequiredMixin, View):

    # Definimos post para poder seguir a un usuario o dejar de seguirlo
    def post(self, request, pk, *args, **kwargs):

        # Obtenemos el perfil al que se va a seguir o dejar de seguir
        profile = Profile.objects.get(pk=pk)

        # Obtenemos el usuario que va a seguir o dejar de seguir
        # Add nos permite agregar un objeto a una relacion muchos a muchos
        profile.followers.add(request.user)

        # Mostrar mensaje de exito en el html
        messages.add_message(
            self.request, 
            messages.SUCCESS, 
            'Siguiendo a {}'.format(profile.user.username
            ))
       
        # Redireccionamos al perfil del usuario
        return redirect('users:profile', username = request.user.username)
    



# Creamos una vista para dejar de seguir a un usuario
class RemoveFollower(LoginRequiredMixin, View):

    # Definimos post para poder dejar de seguir a un usuario
    def post(self, request, pk, *args, **kwargs):

        # Obtenemos el perfil al que se va a dejar de seguir
        profile = Profile.objects.get(pk=pk)

        # Obtenemos el usuario que va a dejar de seguir
        # Remove nos permite eliminar un objeto de una relacion muchos a muchos
        profile.followers.remove(request.user)

        # Mostrar mensaje de exito en el html
        messages.add_message(
            self.request, 
            messages.SUCCESS, 
            'Dejaste de seguir a {}'.format(profile.user.username
            ))
       
        # Redireccionamos al perfil del usuario
        return redirect('users:profile', username = request.user.username)
    



# Creamos una vista para mostrar los seguidores de un usuario
class ListFollowers(View):

    # Definimos get para poder mostrar los seguidores de un usuario
    def get(self, request, pk, *args, **kwargs):

        # Obtenemos el perfil del usuario
        profile = Profile.objects.get(pk=pk)

        # Obtenemos los seguidores del usuario
        # All nos permite obtener todos los objetos de una relacion muchos a muchos
        followers = profile.followers.all()


        # Obtenemos el contexto
        context = {

            # Obtenemos el perfil del usuario
            'profile':profile,

            # Obtenemos los seguidores del usuario
            'followers':followers
        }

        # Retornamos y renderizamos los seguidores del usuario
        return render(request, 'pages/social/followers_list.html', context)