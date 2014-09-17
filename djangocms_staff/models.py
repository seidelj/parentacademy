
from cms.models import CMSPlugin
from django.db import models
from staff.models import Staff

class StaffPlugin(CMSPlugin):
    staff = models.ForeignKey(Staff)

    def __unicode__(self):
        return self.staff.firstname


