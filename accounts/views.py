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
    


# Creamos una vista para editar el perfil del usuario
# Login_required: Es un decorador que nos permite restringir el acceso a una vista
@login_required
def EditProfile(request):

    # Identificamos que el usuario logueado es el mismo que el perfil que se va a editar
    user = request.user.id

    # Obtenemos el perfil del usuario
    profile = Profile.objects.get(user__id=user)

    # Obtenemos la informacion del usuario logueado
    user__info = User.objects.get(id=user) 


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
            user__info.first_name = form.cleaned_data.get['first_name']
            user__info.last_name = form.cleaned_data.get['last_name']


            # Pasaremos a editar el perfil del usuario
            # hacemos referencia a la imagen de perfil del usuario
            profile.picture = form.cleaned_data.get['picture']

            # hacemos referencia a la imagen de banner del usuario
            profile.banner = form.cleaned_data.get['banner']

            # hacemos referencia a la ubicacion del usuario
            profile.location = form.cleaned_data.get['location']

            # hacemos referencia a la sitio web del usuario
            profile.website = form.cleaned_data.get['website']

            # hacemos referencia a la fecha de nacimiento del usuario
            profile.birthday = form.cleaned_data.get['birthday']

            # hacemos referencia a la biografia del usuario
            profile.biography = form.cleaned_data.get['biography'] 


            # Guardamos los cambios
            # Guardamos los cambios del usuario
            user__info.save()

            # Guardamos los cambios del perfil
            profile.save()

            # Redireccionamos al perfil del usuario
            return redirect('users:detail', request.user.username)
        
    # Si el metodo es GET
    else:

        # Obtenemos el formulario para editar el perfil
        form = EditProfileForm(instance=profile)


    # Obtenemos el contexto
    context = {

        # Obtenemos el formulario para editar el perfil
        'form':form
    }

    # Retornamos y renderizamos el formulario para editar el perfil
    return render(request, 'users/edit.html', context)