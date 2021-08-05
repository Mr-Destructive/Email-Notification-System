from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView 
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

from .serializers import ScheduledMailSerializer
from .models import ScheduledMail

# Create your views here.

class Create_Mail(CreateAPIView):
    serializer_class = ScheduledMailSerializer
    def post(self, request, format = None):
        serializer = ScheduledMailSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            
        return Response(serializer.data)    

