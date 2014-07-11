from django.db import models
from cms.models import CMSPlugin
from calender.models import Events
# Create your models here.
# THIS IS SOME CMS STUFF

class CalenderPlugin(CMSPlugin):
	events = models.ForeignKey(Events)

	def __unicode__(self):
		return self.events.title

	