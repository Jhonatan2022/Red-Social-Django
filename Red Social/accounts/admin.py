# Importamos el modelo admin de django para poder crear un modelo de administración
from django.contrib import admin

# Importamos los modelos de User y Profile para poder mostrarlos en el panel de administración
from .models import User, Profile
# Register your models here.
#--------------------------IMPORT OF MODELS------------------------------#




#--------------------------PARA EL PANEL DE ADMINISTRACIÓN-------------------#
# Usamos register para registrar el modelo User en el panel de administración
admin.site.register(User)




# Usamos register para registrar el modelo Profile en el panel de administración
admin.site.register(Profile)

