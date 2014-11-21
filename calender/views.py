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
	events_list = Events.objects.filter(council=campus).filter(eventdate__gte=day.today).order_by('eventdate','start')[:10]
	noEvents = True if not events_list else False
	context = { 'events': events_list, 'noEvents': noEvents, 'message': message, 'name': name, 'campus': campus, }
	return render(request, 'calender/base.html', context)

def schedule_group(request, campus, color):
	message = "No upcoming event"
	if campus != "c" and campus != "m":
		raise Http404
	name = "Camden" if campus == "c" else "MiddlesBrough"
	events_list = Events.objects.filter(council=campus).filter(eventdate__gte=day.today).filter(color="#{}".format(color)).order_by('eventdate', 'start')[:10]
	noEvents = True if not events_list else False
	context = { 'events': events_list, 'noEvents': noEvents, 'message': message, 'name': name, 'campus': campus }
	return render(request, 'calender/base.html', context)

