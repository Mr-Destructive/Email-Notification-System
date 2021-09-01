from django.urls import path
from .views import MailView

urlpatterns = [
        path('<int:pk>', MailView.as_view(), name='mail'),  
]
