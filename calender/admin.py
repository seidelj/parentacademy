from django.contrib import admin
from calender.models import Events 

# Register your models here


class EventsAdmin(admin.ModelAdmin):
	
	fieldsets = [
	    ("Event Information", {'fields': ['council', 'location', 'group', 'color']}),
	    ("Date and Time",	{'fields': ['date', 'start', 'end']}),
	]

	list_display = ('group', 'date', 'council')
	list_filter = ['council']
	date_hierarchy = 'date'

admin.site.register(Events, EventsAdmin)
