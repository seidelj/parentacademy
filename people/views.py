from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import generic

from .models import PeoplePluginModel

# Create your views here.

class DetailView(generic.DetailView):
	model = PeoplePluginModel
	template_name = 'people/detail.html'
	
	def get_queryset(self):
		return Poll.objects.all()
