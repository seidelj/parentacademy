from django.db import models
from cms.models import CMSPlugin

class Events(models.Model):	

	CAMPUS_CHOICES = (
		('c', 'Camden'),
		('m', "Middlesbrough"),
	)

	GROUP_CHOICES = (
		('Year 3 & 4', 'Year 3 & 4'),
		('Year 5 & 6', 'Year 5 & 6'),
	)

	COLOR_CHOICES = (
		('#ef4a2d', 'red'),
		('#1ca6bc', 'blue'),
		('#f99e35', 'orange'),
		('#87be62', 'green'),
	)
	
	council = models.CharField(max_length=3, choices=CAMPUS_CHOICES)
	date = models.DateField("Date")
	start = models.CharField("Start Time", max_length=128)
	end = models.CharField("End Time", max_length=128)
	title = models.CharField("Event Title", max_length=256)
	location = models.TextField("Event Location")
	group = models.CharField(max_length=128, choices=GROUP_CHOICES)
	color = models.CharField(max_length=128, choices=COLOR_CHOICES)
	
	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = 'Event'	
		verbose_name_plural = "Events"

