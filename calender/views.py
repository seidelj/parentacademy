from django.shortcuts import render, render_to_response
from calender.models import Events
from django.http import Http404
from datetime import date as day
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext

# Create your views here.
def schedule(request, campus):
	message = "No upcoming events"
	if campus != "c" and campus != "m":
		raise Http404
	name = "Camden" if campus == "c" else "Middlesbrough"
	events_list = Events.objects.filter(council=campus).filter(eventdate__gte=day.today).order_by('eventdate','start')
	noEvents = True if not events_list else False
	paginator = Paginator(events_list, 10)
	page = request.GET.get('page')
	print page
	try:
		events = paginator.page(page)
	except PageNotAnInteger:
		events = paginator.page(1)
	except EmptyPage:
		events = paginator.page(paginator.num_pages)

	context = { 'events': events, 'noEvents': noEvents, 'message': message, 'name': name, 'campus': campus, }
	print page
	return render_to_response('calender/base.html', context, context_instance=RequestContext(request))

def schedule_group(request, campus, color):
	message = "No upcoming event"
	if campus != "c" and campus != "m":
		raise Http404
	name = "Camden" if campus == "c" else "MiddlesBrough"
	events_list = Events.objects.filter(council=campus).filter(eventdate__gte=day.today).filter(color="#{}".format(color)).order_by('eventdate', 'start')
	noEvents = True if not events_list else False
	paginator = Paginator(events_list, 10)
	page = request.GET.get('page')
	try:
		events = paginator.page(page)
	except PageNotAnInteger:
		events = paginator.page(1)
	except EmptyPage:
		events = paginator.page(paginator.num_pages)

	context = { 'events': events, 'noEvents': noEvents, 'message': message, 'name': name, 'campus': campus }
	return render_to_response('calender/base.html', context, context_instance=RequestContext(request))

