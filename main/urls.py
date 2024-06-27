from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('app', AppView.as_view(), name='app'),
    path('contact', ContactView.as_view(), name='contact'),
    path('community', CommunityView.as_view(), name='community'),
    path('replays/<int:id>/', ReplayView.as_view(), name='replays'),
]