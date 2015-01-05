from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import PeoplePluginModel

class PeoplePlugin(CMSPluginBase):
	model = PeoplePluginModel
	name = _("People Plugin")
	render_template = 'people/plugin.html'
	
	def render(self, context, instance, placeholder):
		context.update({'instance': instance})
		return context

plugin_pool.register_plugin(PeoplePlugin)

