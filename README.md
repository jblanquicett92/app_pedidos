# Mobilender Pedidos
## _Prueba de programacion_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

 ## Inicio 🚀 
Mobilender pedidos es una RESTful API de un sistema de pedidos recibidos desde clientes. fue creada en el ecosistema de Python:


## Tech

Mobilender usa varias tecnologias open source para que el proyecto funciones correctamente:

- [Python3]
- [Django3]
- [Django rest framework]
- [Postgresql]
- [Docker]
- [Git]
- ✨Magia✨

## Pre requisitos

Mobilender requiere que tengas instalado Python3 y Composer.

Si quieres contribuir o probar el proyecto, recuerda que debes descargar del repositorio este proyecto, aqui dejo un listado recomendado de comandos para que trabajes desde tu terminal favorita.

```sh
sudo apt-get update
sudo apt install python3
sudo apt install python3-django
sudo apt install postgresql postgresql-contrib
sudo apt install pgadmin4
sudo apt install docker-ce docker-ce-cli containerd.io
sudo apt install git
```

## Desarrolladores

¿Quieres contribuir o probar? Genial!

Abre tu terminal favorita y escribe estos comandos.

Primer Tab:

```sh
docker build .
```

Segundo Tab:

```sh
docker-compose build
```

Tercer Tab
```sh
docker-compose up
```

(Opcional) Cuarto Tab:

```sh
docker-compose run app sh -c "python manage.py test"
```

> Note: En el folder de presentacion, hay una guia con los puntos desarrollados.

Verifica el que el software este desplegado en


## Documentación

Cuando el software ya se encuentre desplegado podras ver la documentacion swagger y redoc en las siguientes urls

```sh
http://127.0.0.1:8000/swagger/
```
```sh
http://127.0.0.1:8000/redoc/
```

## Uso de PG4 WEB
Podras gestionar la base de datos con la siguiente url:
```sh
http://127.0.0.1:8889/
```
las credenciales son
```sh
admin@example.com
root
```
MIT
