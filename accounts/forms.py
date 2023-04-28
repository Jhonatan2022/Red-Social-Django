# Usaremos este documento para la poder editar los campos del perfil
# Importamos profile para poder editar los campos del perfil
from accounts.models import Profile

# Importamos forms para poder crear un formulario
from django import forms

# Importamos get_user_model para poder obtener el modelo de usuario
from django.contrib.auth import get_user_model
# -------------------------------IMPORT DE MODELS--------------------------------



# Definimos usuario como el modelo de usuario
User = get_user_model()



# -------------------------------FORMULARIO--------------------------------

# Creamos el formulario para poder editar los campos del perfil
class EditProfileForm(forms.ModelForm):

    # Editamos el first_name del usuario
    # Widget: Es un objeto que se encarga de renderizar un campo de formulario en algo que el usuario puede ver
    first_name = forms.CharField(

        # Usamos el widget para poder editar el campo
        widget=forms.TextInput(attrs={

            # Le insertamos los estilos al campo
            'class': 'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
        }))


    # Editamos el last_name del usuario
    # Widget: Es un objeto que se encarga de renderizar un campo de formulario en algo que el usuario puede ver
    last_name = forms.CharField(

        # Usamos el widget para poder editar el campo
        widget=forms.TextInput(attrs={

            # Le insertamos los estilos al campo
            'class': 'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
        }))


    # Editamos la imagen de perfil del usuario
    picture = forms.ImageField(label='Profile Picture', 
                               required=False, widget=forms.FileInput)


    # Editamos la imagen de banner del usuario
    banner = forms.ImageField(label='Banner Picture',
                              required=False, widget=forms.FileInput)


    # Editamos la ubicacion del usuario
    location = forms.CharField(
        
        # Usamos el widget para poder editar el campo
        widget=forms.TextInput(attrs={

            # Le insertamos los estilos al campo
            'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), 
            max_length=25, required=False)


    # Editamos la url del usuario
    website = forms.URLField(
        label='Website URL',
        
        # Usamos el widget para poder editar el campo
        widget=forms.TextInput(attrs={

            # Le insertamos los estilos al campo
            'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), 
            max_length=60, required=False)


    # Editamos la biografia del usuario
    biography = forms.CharField(
        
        # Usamos el widget para poder editar el campo
        widget=forms.TextInput(attrs={
            
            # Le insertamos los estilos al campo
            'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), 
            max_length=260, required=False)


    # Editamos la fecha de nacimiento del usuario
    birthday = forms.DateField(
        
        # Usamos el widget para poder editar el campo
        widget=forms.TextInput(attrs={
            
            # Le insertamos los estilos al campo
            'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), 
            required=False)
