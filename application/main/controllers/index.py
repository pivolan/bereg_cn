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

from application.library.system.util import render_to
from application.main.models import *

from google.appengine.api import memcache
from google.appengine.api import mail
from google.appengine.api import users as googleUsers

import timeit
import re
import random
import datetime
from datetime import timedelta
import os

class view:
	pass

@render_to("controllers/index/index.html")
def index(request):
	return view.__dict__

def login(request):
	return HttpResponseRedirect(redirect_to = googleUsers.create_login_url('/'))

def logout(request):
	return HttpResponseRedirect(redirect_to = googleUsers.create_logout_url('/'))