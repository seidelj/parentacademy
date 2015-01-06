from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool

from .models import PeoplePluginModel

class PeopleMenu(CMSAttachMenu):
	name = _("People Menu")
	
	def get_nodes(self, request):
		nodes = []
		for people in PeoplePluginModel.objects.all():
			node = NavigationNode(
				people.name,
				reverse('people:detail', args=(people.pk)),
				people.pk
		)
		nodes.append(node)
		return nodes

menu_pool.register_menu(PeopleMenu)

