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


    # Definimos el campo para poder compartir el post
    # TextField para que el campo pueda ser largo
    shared_body = models.TextField(blank=True, null=True)


    # Definimos el campo para poder compartir el post y le pasamos el foreign key del post que esta compartiendo
    # ForeignKey para que un post solo pueda tener un post compartido y un post compartido pueda tener varios posts
    # on_delete=models.CASCADE para que si se elimina el post se eliminen sus compartidos
    # null=True para que no sea obligatorio compartir un post
    # blank=True para que no sea obligatorio compartir un post
    # related_name='+' para que no se pueda acceder a los posts compartidos de un post
    shared_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name='+')


    # Definimos el campor de fecha en que se compartio el post
    # null=True para que no sea obligatorio compartir un post
    # blank=True para que no sea obligatorio compartir un post
    shared_on = models.DateTimeField(null=True, blank=True)


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


    # Definimos el autor del post
    # on_delete=models.CASCADE para que si se elimina el usuario se eliminen sus posts
    # related_name='social_posts_author' para que se pueda acceder a los posts de un usuario
    # ForeignKey para que un post solo pueda tener un autor y un autor pueda tener varios posts
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_posts_author')


    # Definimos los likes del post
    # ManyToManyField para que un post pueda tener varios likes
    # blank=True para que no sea obligatorio dar like
    # related_name='likes' para que se pueda acceder a los likes de un post
    likes = models.ManyToManyField(User, blank=True, related_name='likes')


    # Definimos los dislikes del post
    # ManyToManyField para que un post pueda tener varios dislikes
    # blank=True para que no sea obligatorio dar dislike
    # related_name='dislikes' para que se pueda acceder a los dislikes de un post
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')




# Definimos el modelo de comentarios de los posts 
class SocialComment(models.Model):


    # Definimos los comentarios del post
    # TextField para que el comentario pueda ser largo
    comment = models.TextField()


    # Definimos la fecha de publicación del comentario del post
    # default=timezone.now para que la fecha de publicación sea la fecha actual
    created_on = models.DateTimeField(default=timezone.now)


    # Definimos el autor del comentario del post
    # on_delete=models.CASCADE para que si se elimina el usuario se eliminen sus comentarios
    # related_name='social_comments_author' para que se pueda acceder a los comentarios de un usuario
    # ForeignKey para que un comentario solo pueda tener un autor y un autor pueda tener varios comentarios
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_comments_author')


    # Definimos el post del comentario del post
    # on_delete=models.CASCADE para que si se elimina el post se eliminen sus comentarios
    # related_name='social_comments_post' para que se pueda acceder a los comentarios de un post
    # ForeignKey para que un comentario solo pueda tener un post y un post pueda tener varios comentarios
    post = models.ForeignKey('SocialPost', on_delete=models.CASCADE)


    # Definimos los likes del comentario del post
    # ManyToManyField para que un comentario pueda tener varios likes
    # blank=True para que no sea obligatorio dar like
    # related_name='comment_likes' para que se pueda acceder a los likes de un comentario
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')


    # Definimos los dislikes del comentario del post
    # ManyToManyField para que un comentario pueda tener varios dislikes
    # blank=True para que no sea obligatorio dar dislike
    # related_name='comment_dislikes' para que se pueda acceder a los dislikes de un comentario
    dislikes = models.ManyToManyField(User, blank=True, related_name='comment_dislikes')


    # Definimos el comentario padre del comentario del post
    # on_delete=models.CASCADE para que si se elimina el comentario padre se eliminen sus comentarios hijos
    # related_name='+' para que no se pueda acceder a los comentarios hijos de un comentario
    # ForeignKey para que un comentario solo pueda tener un comentario padre y un comentario padre pueda tener varios comentarios hijos
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')


    # Declaramos una propiedad para saber si el comentario tiene un comentario padre
    # Usamos @property para que se ejecute la función y no se guarde en la base de datos
    # property nos sirve para acceder a la función como si fuera un atributo
    @property

    # Definimos si el comentario tiene un comentario padre
    def children(self):

        # Retornamos todos los comentarios hijos de un comentario padre
        # Usamos all() para que se ejecute la consulta a la base de datos
        # Usamos order_by('-created_on') para que los comentarios hijos se ordenen por fecha de publicación descendente
        return SocialComment.objects.filter(parent=self).order_by('-created_on').all()
    


    # Declaramos una propiedad para saber si el comentario es pariente de otro comentario
    # Usamos @property para que se ejecute la función y no se guarde en la base de datos
    # property nos sirve para acceder a la función como si fuera un atributo
    @property

    # Definimos si el comentario es pariente de otro comentario
    def is_parent(self):

        # Retornamos si el comentario tiene un comentario padre
        if self.parent is None:

            # Retornamos True si el comentario no tiene un comentario padre
            return True
        
        # Retornamos False si el comentario tiene un comentario padre
        return False




# Definimos el modelo de imagenes de los posts
class Image(models.Model):


    # Definimos la imagen del post
    # ImageField para que la imagen sea una imagen
    # upload_to=user_directory_path para que la imagen se suba a la ruta definida en user_directory_path
    # blank=True para que no sea obligatorio subir una imagen
    # null=True para que no sea obligatorio subir una imagen
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)