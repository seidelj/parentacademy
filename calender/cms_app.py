from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class CalenderApp(CMSApp):
	name = _("Calender App")
	urls = ["calender.urls"]
	app_name = "calender"

apphook_pool.register(CalenderApp)
