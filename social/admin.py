from django.contrib import admin

# Importamos los modelos de la aplicación social
from .models import SocialPost, SocialComment

# Register your models here.

# Registramos el modelo SocialPost en el administrador de Django
admin.site.register(SocialPost)

# Registramos el modelo SocialComment en el administrador de Django
admin.site.register(SocialComment)
