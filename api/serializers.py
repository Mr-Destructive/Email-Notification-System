from rest_framework import serializers
from .models import  ScheduledMail


class ScheduledMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledMail
        fields = ('subject','body','send_on','sender','recipients_list','attachment_file')
