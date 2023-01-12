#import os
from email.message import EmailMessage
import datetime
import ssl
import smtplib
from config import *

email_sender = 'juan@juanduque.me'
#email_password = os.getenv("JUANDUQUE_PASS")
email_password = password
email_receiver = ['vgiraldo@ganoexcel.com.co']
email_bcc = ['jduque0289@gmail.com']

monday = datetime.datetime.today() + datetime.timedelta(days=3)
tuesday = datetime.datetime.today() + datetime.timedelta(days=4)
subject = f'Mensaje enviado desde el tester Mac'
body = f'Buenos días Vane,\nEn el siguiente correo solicito amablemente la reserva de la sala de juntas para los siguientes días:\n lunes {monday:%d/%m/%Y} a las 10:15AM \n martes {tuesday:%d/%m/%Y} a las 10:15AM - Reunion Diamantes Medellin\n\nGracias :) y te deseo un feliz día \n\nJuan David Duque Arcila\nDiamante GanoExcel'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Bcc'] = email_bcc
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()


with smtplib.SMTP_SSL('mail.juanduque.me', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_bcc + email_receiver, em.as_string())
    smtp.quit()
