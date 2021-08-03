from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class MailRecipient(models.Model):
    mail_address = models.EmailField(max_length = 255)

    def __str__(self):
        return self.mail_address


class ScheduledMail(models.Model):
    sender = models.EmailField(max_length = 255) 
    subject = models.CharField(max_length = 78)
    body = models.CharField(max_length = 40000)
    send_on = models.DateTimeField(default = timezone.now(), blank=False)
    recipients_list = models.ManyToManyField(MailRecipient, related_name = 'mail_list')
    attachment_file = models.FileField()

    def __str__(self):
        return self.subject
