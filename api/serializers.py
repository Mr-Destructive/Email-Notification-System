from rest_framework import serializers
from .models import  MailRecipient, ScheduledMail


class MailRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailRecipient
        fields = ('mail_address',)
       
class ScheduledMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledMail
        fields = ('subject','body','send_on','sender','recipients_list','attachment_file')
