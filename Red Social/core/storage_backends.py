# Importamos S3Boto3Storage para poder subir archivos a S3
from storages.backends.s3boto3 import S3Boto3Storage
#--------------------------------IMPORT S3Boto3Storage---------------------------------#




#--------------------------------STORAGE BACKENDS---------------------------------#
# Definimos la clase StaticStorage para poder subir archivos a S3 y que sean publicos
class StaticStorage(S3Boto3Storage):

    # Definimos el directorio donde se subirán los archivos
    # Location es el nombre del directorio donde se subirán los archivos
    location = 'static'

    # Defaul_acl es el permiso que tendrán los archivos
    default_acl = 'private'




# Definimos la clase PublicMediaStorage para poder subir archivos a S3 y que sean publicos
class PublicMediaStorage(S3Boto3Storage):

    # Definimos el directorio donde se subirán los archivos
    # Location es el nombre del directorio donde se subirán los archivos
    location = 'media'

    # Defaul_acl es el permiso que tendrán los archivos
    default_acl = 'private'

    # file_overwrite es para que si se sube un archivo con el mismo nombre se sobreescriba
    file_overwrite = False