from django.db import models

# Create your models here.

class Staff(models.Model):
	firstname = models.CharField("First Name", max_length=256)
	lastname = models.CharField("Last Name", max_length=256)
	picture_url = models.CharField("Relative Picture URL", max_length=512)
	publish = models.BooleanField("Publish", default=False) 
	
	def _get_full_name(self):
		return "{} {}".format(self.firstname, self.lastname)
	
	full_name = property(_get_full_name)
	
	def __unicode__(self):
		return self.full_name

