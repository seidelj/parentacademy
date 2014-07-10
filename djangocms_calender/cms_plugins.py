from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from djangocms_calender.models import CalenderPlugin
from django.utils.translation import ugettext as _

class CMSCalenderPlugin(CMSPluginBase):
	model = CalenderPlugin
	module = _("Calender")
	name = _("Calender Plugin")
	render_template = "djangocms_calender/schedule.html"

	def render(self, context, instance, placeholder):
		context.update({'instance': instance})
		return context

plugin_pool.register_plugin(CMSCalenderPlugin)

