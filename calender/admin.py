from django.contrib import admin
from calender.models import Events 

# Register your models here


class EventsAdmin(admin.ModelAdmin):
	fieldsets = [
	    ("Event Information", {'fields': ['title', 'description']}),
	    (None,		{'fields': ['campus']}),
	    ("Date and Time",	{'fields': ['date', 'start', 'end']}),
	]

admin.site.register(Events, EventsAdmin)
