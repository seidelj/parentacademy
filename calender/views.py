from django.shortcuts import render
from calender.models import Events
from django.http import Http404
from datetime import date as day

# Create your views here.
def schedule(request, campus):
	message = "No upcoming events"
	if campus != "c" and campus != "m":
		raise Http404
	name = "Camden" if campus == "c" else "Middlesbrough"
	events_list = Events.objects.filter(campus=campus).filter(date__gte=day.today).order_by('date')[:4]
	noEvents = True if not events_list else False
	context = { 'events': events_list, 'noEvents': noEvents, 'message': message, 'name': name, }
	return render(request, 'calender/base.html', context)