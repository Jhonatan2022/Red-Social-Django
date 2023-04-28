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
    return 'user_{0}/{1}'.format(instance.user.id, filename)
