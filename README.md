# MOBILENDER PEDIDOS

_PRUEBA DE PROGRAMACIÓN

## Inicio 🚀

_Backend de sistema de pedidos recibidos desde clientes ._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_Pyhton, Django, Postgres, docker, git

```
sudo apt-get update
sudo apt install python3
sudo apt install python3-django
sudo apt install postgresql postgresql-contrib
sudo apt install pgadmin4
sudo apt install docker-ce docker-ce-cli containerd.io
sudo apt install git

```

Django Web Framework
django==3.2.5

Django Cors Headers - Used to enable CORS headers in API responses, and allow requests to be made to your API server from other origins.
**django-cors-headers==3.5.0**

Django Rest Framework - Api Logic
**djangorestframework==3.12.4**

PSQL Client - Used as an interface to connect Django application to the POSTGRES.
**psycopg2>=2.7.5, <2.8.0_**


### Instalación 🔧

__Ejecuta:

docker build .
docker-compose build
docker-compose run app sh -c "python manage.py test"
docker-compose up



