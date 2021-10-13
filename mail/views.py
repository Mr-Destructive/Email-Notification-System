from django.shortcuts import render
from api.models import ScheduledMail
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse
from .tasks import sleepy

# Create your views here.
class MailListView(LoginRequiredMixin, ListView):
    model = ScheduledMail
    template_name = 'base.html'

class MailView(LoginRequiredMixin, DetailView):
    model = ScheduledMail
    template_name = 'mail/index.html'

def index(request):
    sleepy.delay(10)
    return HttpResponse('Mail not Sent!')
    
