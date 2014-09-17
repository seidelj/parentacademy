from django.contrib import admin
from staff.models import Staff
# Register your models here.

class StaffAdmin(admin.ModelAdmin):
	model = Staff

admin.site.register(Staff, StaffAdmin)
