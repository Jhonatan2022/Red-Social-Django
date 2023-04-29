# Importamos models para crear los modelos de la base de datos de Django
from django.db import models

# Importamos timezone para las fechas de publicación de los posts
from django.utils import timezone

# Importamos get_user_model para obtener el modelo de usuario actual
from django.contrib.auth import get_user_model
#--------------------------------IMPORT BOOKSTORES---------------------



# Definimos user como el modelo de usuario actual
User = get_user_model()



#--------------------------------MODELS--------------------------------

# Definimos en donde e subiran las imagenes de los posts
def user_directory_path(instance, filename):

    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user/socialpost/{0}'.format(filename)



# Definimos en donde se subiran los mensajes del post
def dm_directory_path(instance, filename):

    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user/messages/{0}'.format(filename)


# Definimos el modelo de los posts
class SocialPost(models.Model):

    # Definimos el cuerpo del post
    body = models.TextField()


    # Definimos la imagen del post
    # ManyToManyField para que un post pueda tener varias imagenes
    # maximum 5 images
    # blank=True para que no sea obligatorio subir una imagen
    image = models.ManyToManyField('Image', blank=True) 


    # Definimos la fecha de publicación del post
    # default=timezone.now para que la fecha de publicación sea la fecha actual
    created_on = models.DateTimeField(default=timezone.now)