# # Python-Simple-Form

Ejemplo simple de un form con validacion de campos.

- Python 3
- Django Framework
- Bootstrap

### Installation

Se requiere [Python3](https://www.python.org/downloads/) v3.8+ para ejecutar.

Se requiere [pip installer](https://pip.pypa.io/en/stable/installing/) v20+ para installar dependencias.

Se requiere [Git](https://git-scm.com/downloads/) v2+ para descargar el proyecto.

una vez teniendo todo, ejecutamos...

```sh
$ mkdir form_python && cd $_
```

Para crear la carpeta

```sh
$ git clone https://github.com/rolloutpk/Python-Simple-Form.git
```

Para bajar el proyecto de github

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

para activar el ambiente virtual

```sh
$ pip install django
$ pip install django-bootstrap3
```

para instalar las dependencias

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

para generar los componentes del proyecto

### Run

```sh
$ python manage.py runserver
```

para desplegar el proyecto

```sh
http://localhost:8000/contact/
```

ruta de acceso

### Todos

- Agregar mas cmpos y validaciones
- Hacer algo con la data validada. :)

## License

MIT

**Free Software, Hell Yeah!**
