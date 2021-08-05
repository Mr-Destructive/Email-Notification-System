from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
        path('', TemplateView.as_view(template_name='mail/index.html'),name='mail'),
]
