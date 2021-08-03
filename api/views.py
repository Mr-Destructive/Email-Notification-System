from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView 
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

from .serializers import  MailRecipientSerializer, ScheduledMailSerializer
from .models import  MailRecipient, ScheduledMail

# Create your views here.

class Create_Mail(CreateAPIView):
    serializer_class = ScheduledMailSerializer
    def post(self, request, format = None):
        serializer = ScheduledMailSerializer(data=request.data)
        if(request.POST.get('sender') == request.user.email):
            if(serializer.is_valid()):
                serializer.save()
            
        return Response(serializer.data)    
        #serializer = self.serializer_class(data = request.data)
        #subject = ScheduledMail(subject = subject)
        #body = ScheduledMail(body = body)
        #sender = request.user.email
        #send_on = ScheduledMail(send_on = send_on)
        #recipients_list = ScheduledMail(recipients_list = recipients_list)

        #subject.save()
        #body.save()
        #seder.save()
        #send_on.save()
        #recipients_list.save()

        #return Response(ScheduledMailSerializer(subject, body, send_on, sender, recipients_list).data, status = status.HTTP_201_CREATED)


        
