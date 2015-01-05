from django.db import models
from cms.models import CMSPlugin
from s3direct.fields import S3DirectField
# Create your models here

CAMPUS_CHOICES = (
	('c', "Camden"),
	('m', 'MiddlesBrough'),
)

class PeoplePluginModel(CMSPlugin):
	name = models.CharField('Name', max_length=256)
	contact = models.CharField('Contact', max_length=256)
	biography = models.TextField()
	council = models.CharField('Council', max_length=3, choices=CAMPUS_CHOICES)
	photo = S3DirectField(dest='imgs')

	def __unicode__(self):
		return self.name

