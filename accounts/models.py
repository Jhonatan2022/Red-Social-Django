# Este documento nos servira para extender la base de datos y las tablas que deseemos
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




#----------------------------VARIABLES GLOBALES----------------------------
# Creamos una función para cuando el usuario quiera subir una imagen de perfil
# La intancia hace referencia al modelo Profile (Usuario) y el filename al nombre del archivo
def user_directory_path_profile(instance, filname):

    # Cremos un apartado para que se cree una carpeta con el nombre del usuario y dentro se guarde la imagen
    # El 0 hace referencia al nombre de usuario
    profile_picture_name = 'user/{0}/profile.jpg'.format(instance.user.username)


    # Definimos la ruta donde se guardará la imagen de perfil
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)


    # Si existe una imagen de perfil la borramos para que no se acumulen
    if os.path.exists(full_path):

        # Borramos la imagen de perfil del usuario
        os.remove(full_path)

    # Devolvemos la ruta donde se guardará la imagen
    return profile_picture_name




# Creamos una variable global para las opciones de verificar el tipo de usuario
# Las opciones son una tupla de tuplas
# La primera posición de la tupla es el valor que se guardará en la base de datos
# La segunda posición de la tupla es el valor que se mostrará en el formulario
VERIFICATION_OPTIONS = (

    # La primera opción es la de no verificado
    # La ingresamos dos veces para que este bien definida la tupla
    ('unverified', 'unverified'),

    # Como segunda opción tendremos la de verificado
    ('verified', 'verified'),
)
#----------------------------VARIABLES GLOBALES----------------------------




#----------------------------MODELS--------------------------------------
# Creamos una función para cuando el usuario quiera subir una imagen de banner
# La intancia hace referencia al modelo Profile (Usuario) y el filename al nombre del archivo
def user_directory_path_banner(instance, filname):

    # Cremos un apartado para que se cree una carpeta con el nombre del usuario y dentro se guarde la imagen
    # El 0 hace referencia al nombre de usuario
    profile_picture_name = 'user/{0}/banner.jpg'.format(instance.user.username)

    # Definimos la ruta donde se guardará la imagen de perfil
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)


    # Si existe una imagen de perfil la borramos para que no se acumulen
    if os.path.exists(full_path):

        # Borramos la imagen de perfil del usuario
        os.remove(full_path)

    # Devolvemos la ruta donde se guardará la imagen
    return profile_picture_name




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
    picture = models.ImageField(default='users/default_profile.jpg', upload_to=user_directory_path_profile)

    # Creamos un campo para el banner del perfil del usuario (imagen de portada)
    banner = models.ImageField(default='users/default_banner.jpg', upload_to=user_directory_path_banner)

    # Creamos un campo para la verificación del usuario (si es verificado o no)
    # choices para indicar las opciones que tendrá el campo
    # default para indicar el valor por defecto
    verified = models.CharField(max_length=10, choices=VERIFICATION_OPTIONS, default='unverified')

    # Crearemos un campo de coins para la monetización de la aplicación (moneda virtual)
    # Usaremos (max_digits para indicar el número de dígitos y decimal_places para indicar el número de decimales)
    # Usamos blank=False para que siempre tenga coins ya sea 0 o más
    coins = models.DecimalField(max_digits=19, decimal_places=2, default=0, blank=False) 

    # Creamos un campo para la fecha de creación del perfil (auto_now_add para que se cree automáticamente)
    created = models.DateField(auto_now_add=True)


    # INFORMACIÓN DEL USUARIO

    # Creamos un campo donde el usuario podrá ingresar en donde se encuentra (ciudad, país, etc)
    # Usamos null=True para que pueda ser nulo en la base de datos
    # blank=True para que no sea obligatorio
    location = models.CharField(max_length=50, null=True, blank=True)

    # Creamos un campo para almacenar la url del perfil del usuario usuario
    # Usamos null=True para que pueda ser nulo en la base de datos
    # blank=True para que no sea obligatorio
    website = models.URLField(max_length=80, null=True, blank=True)

    # Creamos un campo para la fecha de cumpleaños del usuario 
    # Usamos null=True para que pueda ser nulo en la base de datos
    # blank=True para que no sea obligatorio
    birthday = models.DateField(null=True, blank=True)

    # Creamos un campo para la biografía del usuario
    # Usamos null=True para que pueda ser nulo en la base de datos
    # blank=True para que no sea obligatorio
    biography = models.TextField(max_length=150, null=True, blank=True)
#----------------------------MODELS--------------------------------------




#--------------------------PARA EL PANEL DE ADMINISTRACIÓN-------------------#
    # Definimos que información vera el administrador en el panel de administración
    def __str__(self):

        # Devolvemos el nombre de usuario
        return self.user.username
#--------------------------PARA EL PANEL DE ADMINISTRACIÓN-------------------#




#-----------------------GURADANDO Y CREANDO EL PERFIL DEL USUARIO-------------#
# Crearemos una instancia cuando el usuario se registre para crear un perfil 
# Usamos signals para que se cree automáticamente
# **kwargs para que acepte cualquier argumento que le pasemos (no es obligatorio)
def create_user_profile(sender, instance, created, **kwargs):

    # Si el usuario se crea
    if created:

        # Creamos un perfil para el usuario
        Profile.objects.create(user=instance)



# Cremos una función para guardar el perfil del usuario
def save_user_profile(sender, instance, **kwargs):

    # La instancia hace referencia al modelo Profile (Usuario)
    # Guardamos el perfil del usuario
    instance.profile.save()



# Usamos post_save para que se cree el perfil después de que se guarde el usuario
# Usamos connect para conectar la señal con la función
post_save.connect(create_user_profile, sender=User) 


# Usamos post_save para que se guarde el perfil después de que se guarde el usuario
# Usamos connect para conectar la señal con la función
post_save.connect(save_user_profile, sender=User)
#-----------------------GURADANDO Y CREANDO EL PERFIL DEL USUARIO-------------#