from django.urls import path,include
from .views import Create_Mail

urlpatterns = [
        path('send-mail/', Create_Mail.as_view(), name='send')
]
