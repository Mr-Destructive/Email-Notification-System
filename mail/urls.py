from django.urls import path
from .views import MailView, index

urlpatterns = [
        path('<int:pk>', MailView.as_view(), name='mail'),  
        path('celery/', index, name='index')
]
