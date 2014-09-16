from django.shortcuts import render

# Create your views here.

def list_staff(request):
	staff = Staff.objects.filter(publish=True)
