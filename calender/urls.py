from django.conf.urls import patterns, url

from calender import views

urlpatterns = patterns('',
    url(r'^(?P<campus>[a-z]*)/$', views.schedule, name='schedule'),
	url(r'^(?P<campus>[a-z]*)/(?P<color>[a-z0-9]*)/$', views.schedule_group, name='schedule_group'),

)
