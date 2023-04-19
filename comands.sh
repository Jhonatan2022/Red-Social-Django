# Comandos para instalar las dependencias de la aplicación

# PASOS A SEGUIR

# Crear un entorno virtual
python -m venv env
# or virtualenv env

# Activar el entorno virtual
env\Scripts\activate


# Instalar los requerimientos del aplicativo
pip install -r requirements.txt
# or pip install -r requirements.sh

# Creamos el proyecto



# comando para generar archivo con las dependencias
pip freeze > requirements.txt
# or pip freeze > requirements.sh