from django.shortcuts import render
from calender.models import Events
from django.http import Http404

# Create your views here.
def schedule(request, campus):
	message = "No upcoming events"
	if campus != "c" and campus != "m":
		raise Http404
	events_list = Events.objects.filter(campus=campus).order_by('-date')[:5]
	noEvents = True if not events_list else False
	context = {'events': events_list, 'noEvents': noEvents, 'message': message, }
	return render(request, 'calender/base.html', context)
