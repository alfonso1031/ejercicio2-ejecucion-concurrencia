# Ejercicio 2: Ejecución con concurrencia

Este ejemplo prepara el mismo desayuno que el ejercicio secuencial, pero inicia
el café, el pan y los huevos de forma concurrente. asyncio.gather permite que
las tareas avancen mientras esperan; por eso se intercalan sus mensajes y el
tiempo total se acerca a la tarea más larga.

## Requisitos

- Docker

## Ejecutar con Docker

Desde la carpeta raíz del repositorio, construye la imagen:

    docker build -t ejercicio2-concurrencia .

Luego ejecuta el contenedor:

    docker run --rm ejercicio2-concurrencia

## Archivos

- main.py: coordina las tareas con asyncio.
- Dockerfile: construye y ejecuta el programa con Python.
