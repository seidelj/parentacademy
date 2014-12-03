from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from calender.models import CalenderPlugin
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class CMSCalenderPlugin(CMSPluginBase):
	model = CalenderPlugin
	module = _("Calender")
	name = _("Calender Plugin")
	render_template = "calender/schedule.html"

	def render(self, context, instance, placeholder):
		context.update({'instance': instance})
		paginator = Paginator(context['events_list'], 10)
		page = context['request'].GET.get('page')
		try:
			events = paginator.page(page)
		except PageNotAnInteger:
			events = paginator.page(1)
		except EmptyPage:
			events = paginator.page(paginator.num_pages)
		
		context.update({'events': events})
		print context['events']
		return context

plugin_pool.register_plugin(CMSCalenderPlugin)

