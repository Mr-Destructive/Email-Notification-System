from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import ScheduledMail
from .forms import MailForm

from django.core.mail import send_mail
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime    
import smtplib, ssl
import time, os
import json

# Create your views here.

class AddMailView(LoginRequiredMixin, CreateView):
    model = ScheduledMail
    form_class = MailForm
    template_name = 'mail/add.html'
    
    def form_valid(self, form):
        form.instance.sender = self.request.user.email
        
        port = 465
        sender_email = self.request.user.email
        reciever_email = form.instance.recipients_list
        password = self.request.user.profile.gapps_key
        body = form.instance.body
        subject = form.instance.subject

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = ','.join(reciever_email)
        message["Subject"] = subject
        
        message.attach(MIMEText(body, "plain"))
        
        #filename = self.request.FILES['attachment_file'] 
 
        #if request.FILES['attachment_file']:
        #    with open(filename, "rb") as attachment:
        #        part = MIMEBase("application", "octet-stream")
        #        part.set_payload(attachment.read())

        #    encoders.encode_base64(part)

        #    part.add_header(
        #        "Content-Disposition",
        #        f"attachment; filename= {filename}",
        #    )

        #    message.attach(part)
        #    message.attach(filename.name, filename.read(), filename.content_type)

        text = message.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, reciever_email, text)
        return super(AddMailView, self).form_valid(form)


