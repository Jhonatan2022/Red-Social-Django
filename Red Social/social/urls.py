# Importamos path para poder crear las urls
from django.urls import path

# Importamos las vistas de la app para poder usarlas

# PostEditView: Vista de editar los posts
from .views import (

    # UserSearch: Vista de buscar usuarios
    UserSearch,
    
    # PostDetailView: Vista de detalle de los posts
    # PostEditView: Vista de editar los posts
    # PostDeleteView: Vista de eliminar los posts
    # SharePostView: Vista de compartir los posts
    PostDetailView,PostEditView, PostDeleteView, SharePostView, 

    # AddLike: Vista de agregar likes 
    # AddDislike: Vista de agregar dislikes
    AddLike, AddDislike, 

    # CommentReplyView: Vista de responder comentarios
    # CommentEditView: Vista de editar comentarios
    # CommentDeleteView: Vista de eliminar comentarios
    CommentReplyView, CommentEditView, CommentDeleteView, 
    
    # AddCommentDislike: Vista de agregar dislikes a los comentarios
    # AddCommentLike: Vista de agregar likes a los comentarios
    AddCommentDislike, AddCommentLike)
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
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),


    # Declaramos la url de agregar dislikes y le pasamos el pk para poder acceder a los posts mediante la url
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),


    # Declaramos la url de compartir los posts y le pasamos el pk para poder acceder a los posts mediante la url
    path('post/<int:pk>/share', SharePostView.as_view(), name='share-post'),


    # Declaramos la url de eliminar comentarios y le pasamos el pk para poder acceder a los comentarios mediante la url
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),


    # Declaramos la url de editar comentarios y le pasamos el pk para poder acceder a los comentarios mediante la url
    path('post/<int:post_pk>/comment/edit/<int:pk>/', CommentEditView.as_view(), name='comment-edit'),


    # Declaramos la url de agregar likes a los comentarios y le pasamos el pk para poder acceder a los comentarios mediante la url
    path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name='comment-like'),


    # Declaramos la url de agregar dislikes a los comentarios y le pasamos el pk para poder acceder a los comentarios mediante la url
    path('post/<int:post_pk>/comment/<int:pk>/dislike', AddCommentDislike.as_view(), name='comment-dislike'),


    # Declaramos la url de agregar respuestas a los comentarios y le pasamos el pk para poder acceder a los comentarios mediante la url
    path('post/<int:post_pk>/comment/<int:pk>/reply', CommentReplyView.as_view(), name='comment-reply'),


    # Declaramos la url de buscar usuarios y le pasamos el pk para poder acceder a los usuarios mediante la url
    path('search/', UserSearch.as_view(), name='profile-search'),
]