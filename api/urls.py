from django.urls import path,include
from .views import AddMailView

urlpatterns = [
        path('send-mail/', AddMailView.as_view(), name='send')
]
