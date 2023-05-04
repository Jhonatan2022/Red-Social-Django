# Importamos path para poder crear las urls
from django.urls import path

# Importamos las vistas de la app para poder usarlas
# PostDetailView: Vista de detalle de los posts
# PostEditView: Vista de editar los posts
# PostDeleteView: Vista de eliminar los posts
# AddLike: Vista de agregar likes
# AddDislike: Vista de agregar dislikes
from .views import PostDetailView, PostEditView, PostDeleteView, AddLike, AddDislike
#------------------------------IMPORT BOOKSTORES----------------------



# Declaramos el nombre de la app
app_name = 'social'



#------------------------------URLS--------------------------------------

# Declaramos las urls de la app
urlpatterns = [


    # Declaramos la url de detalle de los posts y le pasamos el pk para poder acceder a los posts mediante la url
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),


    # Declaramos la url de editar los posts y le pasamos el pk para poder acceder a los posts mediante la url
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),


    # Declaramos la url de eliminar los posts y le pasamos el pk para poder acceder a los posts mediante la url
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),


    # Declaramos la url de agregar likes y le pasamos el pk para poder acceder a los posts mediante la url
    path('post/<int:pk>/like/', AddLike.as_view(), name='like'),


    # Declaramos la url de agregar dislikes y le pasamos el pk para poder acceder a los posts mediante la url
    path('post/<int:pk>/dislike/', AddDislike.as_view(), name='dislike'),
]