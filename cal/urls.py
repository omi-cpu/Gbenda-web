from django.urls import re_path, path
from . import views
from .views import EventList
app_name = 'cal'
urlpatterns = [
    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    re_path(r'^event/new/$', views.event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    path('event_detail/<int:id>/', EventList.as_view(), name='event_detail'),
]