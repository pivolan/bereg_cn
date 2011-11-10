from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from google.appengine.api import images
from pprint import pprint
from django.conf import settings

from library.system.util import render_to
from application.main.models import *
from application.main.forms import feedback as feedback_form

from google.appengine.api import memcache
from google.appengine.api import mail
from google.appengine.api import users as googleUsers

import timeit
import re
import random
import datetime
from datetime import timedelta
import os

class view: pass


@render_to("controllers/index/index.html")
def index(request, id=None):
	if id:
		view.page = EasyPage.get_by_id(int(id))
	else:
		view.page = EasyPage.all().get()

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
			mail.send_mail(sender=form.email,
			               to=settings.ADMIN_EMAIL,
			               subject=form.title,
			               body=form.text)
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