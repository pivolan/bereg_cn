from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import simplejson
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from google.appengine.api import images
from pprint import pprint
from django.conf import settings

from library.system.util import render_to
from library.system.util import login_required
from application.main.models import *

from google.appengine.api import memcache
from google.appengine.api import mail
from google.appengine.api import users as googleUsers

from library.system.BeautifulSoup import BeautifulStoneSoup

import gdata.docs.data
import gdata.docs.client

import timeit
import re
import random
import datetime
from datetime import timedelta
import os

class view:
	pass

@login_required('/')
@render_to("admin/index.html")
def index(request, resource_id=False):
	if not googleUsers.is_current_user_admin():
		return HttpResponseRedirect(redirect_to=googleUsers.create_login_url('/'))
	return view.__dict__


def docstree(request, resource_id=False):
	response_data = False
	feeds = False
	if request.is_ajax():
		client = gdata.docs.client.DocsClient(source='yourCo-yourAppName-v1')
		client.ssl = True  # Force all API requests through HTTPS
		client.http_client.debug = True  # Set to True for debugging HTTP requests
		client.ClientLogin(settings.DOCS_EMAIL, settings.DOCS_PASS, client.source)

		if 'id' in request.GET:
			resource_id = request.GET['id']
			if resource_id:
				if resource_id.find('folder:') >= 0:
					feeds = client.GetDocList(uri='/feeds/default/private/full/%s/contents?showfolders=true' % resource_id)
		else:
			feeds = client.GetDocList(uri='/feeds/default/private/full?showfolders=true')
			for entry in feeds.entry:
				pass

		if feeds:
			response_data = []
			for entry in feeds.entry:
				item = {
					'data': entry.title.text,
					'metadata': {'id': entry.resource_id.text},
					}
				if entry.get_document_type() == 'folder':
					item['state'] = 'closed'

				response_data.append(item)
	return HttpResponse(simplejson.dumps(response_data), mimetype="application/json")


@render_to("controllers/index/admin.html")
def test(request):
	test_page = EasyPage(title=" Hello, this is first ", content=" hi how are you?")
	test_page.put()
	return view.__dict__


def login(request):
	return HttpResponseRedirect(redirect_to=googleUsers.create_login_url('/'))


def logout(request):
	return HttpResponseRedirect(redirect_to=googleUsers.create_logout_url('/'))