# Importamos models para poder crear nuestras clases que heredan de models.Model
from django.db import models

# Importamos abstractuser para poder extenderlo y añadir campos personalizados
from django.contrib.auth.models import AbstractUser

# Importamos settings para poder acceder a la configuración de nuestro proyecto
from django.conf import settings

# Importamos os para poder acceder a las rutas de nuestro proyecto
import os

# Importamos pil para poder trabajar con imágenes en nuestro proyecto
from PIL import Image

# Importamos post_save para poder crear señales que se ejecuten cuando se cree un usuario nuevo en nuestro proyecto
from django.db.models.signals import post_save
#----------------------------IMPORT BOOKSTORES---------------------------



#----------------------------MODELS--------------------------------------
# Este documento nos servira para extender la base de datos y las tablas que deseemos



# Creamos una función para cuando el usuario quiera subir una imagen de perfil
# La intancia hace referencia al modelo Profile (Usuario) y el filename al nombre del archivo
def user_directory_path_profile(instance, filname):

    # Cremos un apartado para que se cree una carpeta con el nombre del usuario y dentro se guarde la imagen
    # El 0 hace referencia al nombre de usuario
    profile_picture_name = 'user/{0}/profile.jpg'.format(instance.user.username)



# Creamos una clase que hereda de AbstractUser para poder extender el modelo de usuario
class User(AbstractUser):

    # Crearemos un customer id para poder identificar a los usuarios de forma única
    # blank=True para que no sea obligatorio, null=True para que pueda ser nulo en la base de datos
    stripe_customer_id = models.CharField(max_length=50) 
    


# Creamos una clase que hereda de models.Model para poder crear un modelo de perfil de usuario
class Profile(models.Model):

    # Creamos una relación uno a uno con el modelo User Usando el campo OneToOneField
    # on_delete=models.CASCADE para que cuando se borre el usuario se borre el perfil
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # Usamos related_name para poder acceder al perfil desde el usuario

    # Creamos un campo de imagen para poder añadir una imagen de perfil
    # upload_to para indicar la ruta donde se guardará la imagen
    # default para indicar una imagen por defecto
    picture = models.ImageField(upload_to='profile', default='media/users/default.jpg')
