from django.conf.urls import patterns, url

from calender import views

urlpatterns = patterns('',
    url(r'^(?P<campus>[a-z]*)/$', views.schedule, name='schedule'),
)
