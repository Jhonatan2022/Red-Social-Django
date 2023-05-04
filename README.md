# Red-Social-With-Django

## Requisitos previos

* Python instalado [python](https://www.python.org/downloads/release/python-31010/)
* Node instalado [Nodejs](https://nodejs.org/en)
* PostgresSQL [PostgresSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

<HR>

## Creamos la base de datos

1. Ponemos de contraseña en postgreSQL `papichulo`
2. Abrimos pgAdmin 4, dijitamos la contraseña damos click derecho en el Databases, Create y Database

![image](https://user-images.githubusercontent.com/101368711/236312931-8b241ed4-9531-4c0c-a533-ce56d9b443f5.png)

<HR>

## Pasos a seguir
```sh
#Descarga del proyecto
git clone https://github.com/Jhonatan2022/Red-Social-With-Django.git
```
```sh
# Ingresamos a la carpeta
cd '.\Red Social\'
```
<HR>

```sh
# Si no tenemos virtualenv, lo instalamos 
pip install virtualenv
```
```sh
# Creamos un entorno virtual
virtualenv env
```
```sh
# Damos permisos a nuestro sistema para que pueda ejecutar Scripts
# Ejecutamos powerShell como administrador y ponemos:
Set-ExecutionPolicy RemoteSigned
```
```sh
# Activamos el entorno virtual
env\Scripts\activate
```
```sh
# Instalamos las dependencias del app
pip install -r requirements.sh
```
<HR>

```sh
# Migramos todo a la base de datos
python manage.py migrate
```

## Pasos para correr el aplicativo

```sh
# Instalamos tailwind para los estilos
python manage.py tailwind install
```
```sh
# Inicializamos tailwind CSS
python manage.py tailwind start
```
```sh
# Ejecutamos el aplicativo
python manage.py runserver
```
<HR>

## Basado en: [Apholdings](https://github.com/apholdings/Django-Red-Social)
## Modificado por: [Jhonatan2022](https://github.com/Jhonatan2022/Red-Social-With-Django)