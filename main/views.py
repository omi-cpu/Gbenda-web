from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.


class IndexView(ListView):
    model = Home
    template_name = 'index.html'

class AboutView(ListView):
    model = Home
    template_name = 'about.html'

class AppView(ListView):
    model = Home
    template_name = 'app.html'

class ContactView(ListView):
    model = Home
    template_name = 'contact.html'

class CommunityView(ListView):
    model = BibleStudy
    template_name = 'community.html'
    queryset = BibleStudy.objects.all()

class ReplayView(ListView):
    model = Replay
    template_name = 'replay_bs.html'
    # queryset = Replay.objects.where()

    def get_queryset(self):
        series = BibleStudy.objects.get(id=self.kwargs['id'])
        return Replay.objects.filter(series=series)

