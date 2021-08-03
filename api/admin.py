from django.contrib import admin
from .models import  MailRecipient, ScheduledMail

# Register your models here.
admin.site.register(ScheduledMail)
admin.site.register(MailRecipient)
