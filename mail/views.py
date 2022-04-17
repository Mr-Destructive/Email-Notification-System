from django.shortcuts import render
from api.models import ScheduledMail
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse


class MailListView(LoginRequiredMixin, ListView):
    model = ScheduledMail
    template_name = "base.html"


class MailView(LoginRequiredMixin, DetailView):
    model = ScheduledMail
    template_name = "mail/index.html"
