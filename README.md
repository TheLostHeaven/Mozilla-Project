# Mozilla-Project (Ejemplo de Li)

![Logo](https://static.djangoproject.com/img/logos/django-logo-negative.svg)

![Logo](https://www.python.org/static/community_logos/python-logo-inkscape.svg)


## Descripción

Este proyecto es un ejemplo de una API RESTful desarrollada con Django que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en un modelo de productos 

## Funcionalidades

- Obtener todos los datos de la DB en la pagina de inicio
- Obtener libros, Autores, Estado del libro, Generos e Idioma de la libreria
- Crear libros, Autores, Estado del libro, Generos e Idioma de la libreria


## Tecnologías utilizadas

- Python
- Django
- Django REST Framework

## Instalación

1. Clona este repositorio en tu máquina local:

```bash
- $ git clone https://github.com/TheLostHeaven/Mozilla-Project
```
2. Navega al directorio del proyecto:

```bash
- $ cd locallibrary
```
3. Puedes cambiar el origen del proyecto con los siguientes comand

```bash
- $ git remote -v
- $ git remote remove origin
- $ git remote add origin <nueva_url_del_repositorio>
```

4. Instalar venv (O el entorno de preferencia)
- Windows:
```bash
- $ python -m venv venv
```
- Linux/Mac
```bash
- $ python3 -m venv venv
```

5. Instala las dependencias necesarias:

```bash
- $ pip install -r requirements.txt
```


## Uso

1. Inicia la aplicación:

- Windows:

```bash
- $ py manage.py runserver 
```

- Linux/Mac:

```bash
- $ python3 manage.py runserver
```

2. Accede a la documentación de la API en tu navegador:

http://localhost:8000/admin


3. Prueba las diferentes rutas disponibles para realizar operaciones CRUD en el Ejemplo de la libreria 

## Contacto

Si tienes alguna pregunta o sugerencia o quieres el workbook para desarrollar este proyecto, no dudes en contactarme en [tiquedaniel2002@gmail.com](tiquedaniel2002@gmail.com).


## Autors

- [@Daniel Molina](https://github.com/TheLostHeaven)
