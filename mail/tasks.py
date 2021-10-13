from celery import shared_task
from django.http import HttpResponse

import smtplib, ssl
from time import sleep
import time
from datetime import datetime    
from django.utils import timezone
import json
from django.core.mail import send_mail
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


@shared_task
def sleepy(duration):
    sleep(duration)
    return HttpResponse("Hello")

@shared_task
def c_sendmails(sender_email, reciever_email, password, message, send_time):
    port = 465
    now_time = datetime.now().replace(tzinfo=None)
    difference = (send_time.replace(tzinfo=None) - now_time).total_seconds()
    sleep(difference)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, reciever_email, message)

