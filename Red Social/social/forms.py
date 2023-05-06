# Usaremos este documento para crear un formulario que nos permita crear posts

# Importamos forms y el modelo Post para poder crear el formulario
from django import forms

# Importamos los modelos de SocialPost y SocialComment para poder crear los formularios
from .models import SocialPost, SocialComment
# -----------------------------IMPORT FORMS-------------------------------------




# -----------------------------CREATE FORMS-------------------------------------
# Creamos el formulario para crear posts
class SocialPostForm(forms.ModelForm):

    # Definimos el cuerpo del post como un campo de texto
    # CharField para que el cuerpo del post sea un campo de texto corto
    # widget=forms.Textarea para que el cuerpo del post sea un campo de texto largo
    # attrs nos permite añadir atributos al campo de texto
    body = forms.CharField(
        widget=forms.Textarea(attrs={

            # Definimos el estilo del campo de texto
            'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md',
            'rows': '3',
            'placeholder': 'Say Something...'
        }),
        # Usamos required=True para que el campo de texto sea obligatorio
        required=True)


    # Definimos la imagen del post
    # FileField para que la imagen del post sea un campo de archivo
    # ClearableFileInput para que se pueda eliminar la imagen del post
    image = forms.FileField(

        # Definimos el estilo del campo de imagen
        widget=forms.ClearableFileInput(attrs={

            # Definimos el estilo del campo de imagen
            'class': 'relative dark:text-dark-txt dark:bg-dark-second cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500',
            'multiple': True
        }),
        # Usamos required=False para que el campo de imagen no sea obligatorio
        required=False)


    # Definimos la clase Meta para el formulario de crear posts
    class Meta:

        # Definimos el modelo del formulario que vamos a editar
        model = SocialPost

        # fields nos permite definir los campos del formulario que vamos a editar
        fields = ['body']




# Creamos el formulario para crear comentarios
class SocialCommentForm(forms.ModelForm):

    # Definimos el cuerpo del comentario como un campo de texto
    # CharField para que el cuerpo del comentario sea un campo de texto corto
    # widget=forms.Textarea para que el cuerpo del comentario sea un campo de texto largo
    # attrs nos permite añadir atributos al campo de texto
    comment = forms.CharField(
        widget=forms.Textarea(attrs={

            # Definimos el estilo del campo de texto
            'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md',
            'rows': '1',
            'placeholder': 'Comment Something...'
        }),
        # Usamos required=True para que el campo de texto sea obligatorio
        required=True)


    # Definimos la clase Meta para el formulario de crear comentarios
    class Meta:

        # Definimos el modelo del formulario que vamos a editar
        model = SocialComment

        # fields nos permite definir los campos del formulario que vamos a editar
        fields = ['comment']




# Creamos un formilario para poder compartir posts
class ShareForm(forms.Form):

    # Definimos el cuerpo del post como un campo de texto
    body = forms.CharField(
        label='',

        # Usamos widget=forms.Textarea para que el cuerpo del post sea un campo de texto largo
        widget=forms.Textarea(attrs={

            # Definimos el estilo del campo de texto
            'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md',
            'rows': '3',
            'placeholder': 'Say Something...'
            }),
        )