from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.utils.encoding import force_unicode, smart_unicode, smart_str
from google.appengine.api import images
from pprint import pprint
from django.conf import settings

from library.system.util import render_to
from application.main.models import *
from application.main.forms import feedback as feedback_form

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
import base64


class view: pass


@render_to("controllers/index/index.html")
def index(request, id=None):
	if id:
		view.page = EasyPage.get_by_id(int(id))
	else:
		view.page = EasyPage.all().get()

	return view.__dict__


@render_to("controllers/index/docs.html")
def docs(request, id=None):
	client = gdata.docs.client.DocsClient(source='yourCo-yourAppName-v1')
	client.ssl = True  # Force all API requests through HTTPS
	client.http_client.debug = True  # Set to True for debugging HTTP requests
	client.ClientLogin('pivo@pivolan.ru', '*****', client.source)
	feeds = view.feeds = client.GetDocList(uri='/feeds/default/private/full?max-results=5')

	view.entry = client.GetFileContent('/feeds/download/documents/Export?id=1ebCRp9Q0_7bxNwtAZr4XYC2sGOdXk3ij6kEpmi-P64Y&format=html')
	html = BeautifulStoneSoup(view.entry, convertEntities=BeautifulStoneSoup.HTML_ENTITIES)
	view.body = html.body.renderContents()
	view.style = html.style.prettify()
	return view.__dict__


@render_to("controllers/index/contacts.html")
def contacts(request):
	return {}


@render_to("controllers/index/study.html")
def study(request):
	return {}


@render_to("controllers/index/service.html")
def service(request):
	return {}


@render_to("controllers/index/feedback.html")
def feedback(request):
	if request.method == "POST":
		form = feedback_form(request.POST)
		if form.is_valid():
			mail.send_mail(sender=form.cleaned_data['email'],
			               to=settings.ADMIN_EMAIL,
			               subject=form.cleaned_data['title'],
			               body=form.cleaned_data['text'])
	else:
		initial_data = {}
		if request.user:
			user = request.user
			initial_data = {
				'company': user.company,
				'address': user.address,
				'phone': user.phone,
				'fio': user.fio,
				'email': user.email(),
				}
		form = feedback_form(initial=initial_data)

	return {'form': form}


def login(request):
	return HttpResponseRedirect(redirect_to=googleUsers.create_login_url('/'))


def logout(request):
	return HttpResponseRedirect(redirect_to=googleUsers.create_logout_url('/'))


@render_to("controllers/index/test.html")
def test(request):
	return {}


@render_to("controllers/index/empty.html")
def empty(request):
	return {}