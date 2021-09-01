from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from datetime import datetime    
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
# Create your models here.


class ScheduledMail(models.Model):
    sender = models.EmailField(max_length = 255) 
    subject = models.CharField(max_length = 78)
    body = models.CharField(max_length = 40000)
    send_on = models.DateTimeField(default = datetime.now(),blank=True)
    recipients_list = ArrayField(models.EmailField(max_length = 255))

    attachment_file = models.FileField(blank=True, null=True)

    @classmethod
    def get_today_mail(cls):
        today = date.today()
        return cls.objects.filter(send_on__year = today.year, send_on__month = today.month, send_on__day = today.day)

    def send_scheduled_mail(self):
        recipient_list = list(self.recipients_list.values_list('mail_address', flat = True))
        mail_msg = EmailMessage(
                subject = self.subject,
                body = self.body,
                from_email = self.sender,
                to = recipient_list,
        )
        mail_msg.content_subtype = 'html'

        mail_msg.send()


    def get_absolute_url(self):  
        return reverse('mail', args=(str(self.id),))


    def __str__(self):
        return self.subject
