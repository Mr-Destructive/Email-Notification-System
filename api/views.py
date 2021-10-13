from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
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

from django.utils import timezone
from mail.tasks import sendmails

from time import sleep
from datetime import tzinfo, timedelta, datetime

ZERO = timedelta(0)

class UTC(tzinfo):
  def utcoffset(self, dt):
    return ZERO
  def tzname(self, dt):
    return "UTC"
  def dst(self, dt):
    return ZERO

utc = UTC()

# Create your views here.
def handle_uploaded_file(f):  
    destination = 'mail/uploads/'
    with open(f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  
            

def sendmails(sender_email, reciever_email, password, message, send_time):
    port = 465
    now_time = datetime.now().replace(tzinfo=None)
    difference = (send_time.replace(tzinfo=None) - now_time).total_seconds()
    print(difference)
    sleep(difference)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, reciever_email, message)


def a_sendmails(sender_email, reciever_email, password, message, send_time):
    difference = send_time - datetime.now(timezone.utc)

def till_redirect():
    return redirect('/')
    

class AddMailView(LoginRequiredMixin, CreateView):
    model = ScheduledMail
    form_class = MailForm
    template_name = 'mail/add.html'
    
    def form_valid(self, form):
        super(AddMailView, self).form_valid(form)
        form.instance.sender = self.request.user.email
        send_time = form.instance.send_on
        
        port = 465
        sender_email = self.request.user.email
        reciever_email = form.instance.recipients_list
        password = self.request.user.gapps_key
        body = form.instance.body
        subject = form.instance.subject

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = ','.join(reciever_email)
        message["Subject"] = subject
        
        message.attach(MIMEText(body, "plain"))
        

        file = form.instance.attachment_file

        
        if file:
            handle_uploaded_file(file)            
            with open(file.name,"rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            encoders.encode_base64(part)

            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {file}",
            )

            
            message.attach(part)
            
        message = message.as_string()

        '''
        loop = asyncio.new_event_loop()
        async def create_tasks_func():
            tasks = list()
            tasks.append(asyncio.create_task(a_sendmails(sender_email, reciever_email, password, message, send_time)))
            await asyncio.wait(tasks)

        loop.run_until_complete(create_tasks_func())
        loop.close()
        '''
        
        sendmails(sender_email, reciever_email, password, message, send_time)

        return super(AddMailView, self).form_valid(form)
        

