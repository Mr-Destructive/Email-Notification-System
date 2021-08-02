from django.db import models
from django.utils import timezone

# Create your models here.

class MailAttachment(models.Model):
    attachment_file = models.FileField()
    attached_to = models.ForeignKey('ScheduledMail', related_name = 'attachments', on_delete = models.CASCADE)

    def __str__(self):
        return '%s (%s)' % (self.attachment_file.filename, self.attached_to.subject)


class MailRecipient(models.Model):
    mail_address = models.EmailField(max_length = 255)

    def __str__(self):
        return self.mail_address


class ScheduledMail(models.Model):
    subject = models.CharField(max_length = 78)
    body = models.CharField(max_length = 40000)
    send_on = models.DateTimeField(default = timezone.now())
    recipients_list = models.ManyToManyField(MailRecipient, related_name = 'mail_list')

    def __str__(self):
        return self.subject
