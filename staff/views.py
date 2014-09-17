from django.shortcuts import render
from staff.models import Staff
# Create your views here.

def list_staff(request):
	staff = Staff.objects.filter(publish=1)
	context = { 'staff': staff, }
	return render(request, 'staff/base.html', context)

