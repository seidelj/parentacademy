from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from djangocms_staff.models import StaffPlugin
from django.utils.translation import ugettext as _

class CMSStaffPlugin(CMSPluginBase):
	model = StaffPlugin
	module = _("Staff")
	name = _("Staff Plugin")
	render_template = "djangocms_staff/staff_plugin.html"

	def render(self, context, instance, placeholder):
		context.update({'instance': instance})
		return context

plugin_pool.register_plugin(CMSStaffPlugin)


