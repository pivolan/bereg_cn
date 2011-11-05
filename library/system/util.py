from django.shortcuts import render_to_response
from django.template import RequestContext

def render_to(template):
	def renderer(function):
		def wrapper(request, *args, **kwargs):
			output = function(request, *args, **kwargs)
			if not isinstance(output, dict):
				return output
			tmpl = output.pop('TEMPLATE', template)
			return render_to_response(tmpl, output, context_instance=RequestContext(request))

		return wrapper

	return renderer


class AuthenticationMiddleware(object):
	def process_request(self, request):
		assert hasattr(request,
		               'session'), "The Django authentication middleware requires session middleware to be installed. Edit your MIDDLEWARE_CLASSES setting to insert 'django.contrib.sessions.middleware.SessionMiddleware'."

		from auth import getCurrentUser

		request.user = getCurrentUser()
		from google.appengine.api import users
		
		request.is_admin = users.is_current_user_admin()
		return None
