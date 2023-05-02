# Importamos path para poder crear las urls
from django.urls import path
#------------------------------IMPORT BOOKSTORES----------------------

# Declaramos el nombre de la app
app_name = 'social'


#------------------------------URLS--------------------------------------

# Declaramos las urls de la app
urlpatterns = [

    # Declaramos la url para poder editar los posts
    # path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
]
