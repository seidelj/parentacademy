from django.contrib import admin
from calender.models import Events 

# Register your models here


class EventsAdmin(admin.ModelAdmin):
	
	fieldsets = [
	    ("Event Information", {'fields': ['council', 'location', 'group', 'color']}),
	    ("Date and Time",	{'fields': ['eventdate', 'start', 'end']}),
	]

	list_display = ('group', 'eventdate', 'council')
	list_filter = ['council']
	date_hierarchy = 'eventdate'

admin.site.register(Events, EventsAdmin)
