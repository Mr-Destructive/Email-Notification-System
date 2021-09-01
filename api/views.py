from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from rest_framework.response import Response
from django.http import JsonResponse
import json
from .models import ScheduledMail
from .forms import MailForm

# Create your views here.

class AddMailView(LoginRequiredMixin, CreateView):
    model = ScheduledMail
    form_class = MailForm
    template_name = 'mail/add.html'
    
    def form_valid(self, form):
        form.instance.sender = self.request.user.email
        return super(AddMailView, self).form_valid(form)


