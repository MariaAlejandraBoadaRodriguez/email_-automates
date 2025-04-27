# Enviar Correos a Clubes Deportivos

Este proyecto permite enviar correos electrónicos a varios clubes deportivos para solicitar información sobre la matrícula y otros valores relacionados con el fútbol para niños de 6 años.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura de archivos:


## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener Python instalado en tu máquina. Si no lo tienes, puedes descargarlo e instalarlo desde [python.org](https://www.python.org/downloads/).

Ademas de subir en la carpeta "data" el excel donde estan los correos destino.

### Dependencias necesarias

Para instalar las dependencias necesarias para este proyecto, abre la terminal y ejecuta:

## Configuración

1. **Correo de envío**: Este proyecto está configurado para usar una cuenta de Gmail para enviar los correos. Asegúrate de **habilitar la verificación en dos pasos** en tu cuenta de Google y generar una **contraseña de aplicación**. Si no sabes cómo hacerlo, sigue los pasos [aquí](https://myaccount.google.com/apppasswords).

2. **Archivo Excel**: El archivo `xxx.xlsx` debe contener los datos de los destinatarios. Este archivo debe estar ubicado en la carpeta `data`. Asegúrate de que el archivo tenga las siguientes columnas (En este caso de clubs deportivos):

    - **Nombre del club deportivo**: El nombre del club. (Destinatario)
    - **Correo electrónico**: El correo de contacto del club. (Correo destino)

3. **Modificar el código**: Asegúrate de que el correo de envío y la contraseña de aplicación estén correctamente configurados en el código, así como la ruta del archivo Excel (`data/clubs.xlsx`).

```python
sender_email = 'tu_correo@gmail.com'
sender_password = 'tu_contraseña_de_aplicación'

