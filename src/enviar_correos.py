import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

# Ruta del archivo Excel con los datos de los clubes (asegúrate de que este archivo esté en la carpeta correcta)
excel_file_path = 'data/clubs.xlsx'  # Cambia la ruta si es necesario
data_sheet = pd.read_excel(excel_file_path, sheet_name='Hoja1') # Cambia nombre de la hoja si es necesario

# Configuración del servidor SMTP de Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'tu_correo@gmail.com'  # Reemplaza con tu correo
sender_password = 'Contraseña de aplicación generada por Google'

# Función para enviar el correo
def send_email(receiver_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Cuerpo del mensaje
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Conexión con el servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Seguridad de la conexión
        server.login(sender_email, sender_password)
        text = msg.as_string()

        # Enviar el correo
        server.sendmail(sender_email, receiver_email, text)
        print(f"Correo enviado a: {receiver_email}")
    except Exception as e:
        print(f"Error al enviar correo a {receiver_email}: {e}")
    finally:
        server.quit()

# Crear el mensaje
subject = "Solicitud de información sobre matrícula"

# Bucle para enviar el correo a cada club
for index, row in data_sheet.iterrows():
    club_name = row['Nombre del club deportivo']
    email = row['Correo electr¢nico']

    # Cuerpo del mensaje
    body = f"""
    Estimados miembros del {club_name},

    Espero que se encuentren bien. Mi nombre es Sofia y me gustaría obtener más información sobre la matrícula y otros valores relacionados con la práctica de fútbol para un niño de 6 años. 

    Agradecería mucho si pudieran proporcionarme detalles sobre los siguientes aspectos:

    - Valor de la matrícula para niños de 6 años.
    - Requisitos para la inscripción en el club.
    - Horarios y días de entrenamiento.
    - Cualquier otra información relevante.

    Quedo atenta/o a su respuesta.

    Muchas gracias por su tiempo y atención.

    Saludos cordiales,
    Sofia
    """

    # Llamada a la función para enviar el correo
    send_email(email, subject, body)
