from django.db import models
from cms.models import CMSPlugin

class Events(models.Model):	

	CAMPUS_CHOICES = (
		('c', 'Camden'),
		('m', "Middlesbrough"),
	)
	
	campus = models.CharField("Campus",max_length=3, choices=CAMPUS_CHOICES)
	date = models.DateField("Event Date")
	start = models.CharField("Start Time", max_length=128)
	end = models.CharField("End Time", max_length=128)
	title = models.CharField("Event Title", max_length=256)
	description = models.TextField("Event Description")

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = 'Event'	
		verbose_name_plural = "Events"

