from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from .menu import PeopleMenu

class PeopleApp(CMSApp):
	name = _("People App")
	urls = ['people.urls']
	app_name = "people"
	menus = [PeopleMenu]

apphook_pool.register(PeopleApp)
