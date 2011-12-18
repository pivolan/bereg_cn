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

from library.system.BeautifulSoup import BeautifulStoneSoup

import gdata.docs.data
import gdata.docs.client

import timeit
import sys
import re
import random
import datetime
from datetime import timedelta
import os
import base64


class view: pass

pages = {
	'main': '1Y4XCUWEriqaDDjVYjJ0nzRsJL9XUDk1tokM6VKqHFaI',
	}


def index(request, q=None):
	page = 'main'
	result = {}
	if q:
		result_id = _get_doc_id_by_q(q)
		print result_id
		if result_id:
			if result_id['is_folder']:
				return catalogue(request, result_id['item'])
			elif result_id['is_document']:
				return document(request, result_id['id'])

	return document(request, pages[page])


@render_to("main/docs.html")
def document(request, id):
	return _get_doc(id)


@render_to("main/catalogue.html")
def catalogue(request, folder_gdata_item):
	view.feeds = get_doc_list(
		uri='/feeds/default/private/full/%s/contents?showfolders=true' % folder_gdata_item.resource_id.text)
	view.folder = folder_gdata_item
	return view.__dict__


@render_to("main/contacts.html")
def contacts(request):
	return {}


@render_to("main/study.html")
def study(request):
	return {}


@render_to("main/service.html")
def service(request):
	return {}


@render_to("main/feedback.html")
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


def _get_doc(id, use_cache=True):
	if googleUsers.is_current_user_admin():
		memcache.delete(id)

	result = memcache.get(id)
	if not result:
		entry = get_exported_gdoc(id)

		html = BeautifulStoneSoup(entry, convertEntities=BeautifulStoneSoup.HTML_ENTITIES)

		head_title = ''
		keywords = ''
		description = ''

		if html.body.div:
			head_title = html.body.div.find(text=re.compile("title = .*"))
			keywords = html.body.div.find(text=re.compile("keywords = .*"))
			description = html.body.div.find(text=re.compile("description = .*"))
		title = html.head.title.text

		if head_title:
			head_title = head_title.replace("title = ", '')
		else:
			head_title = title
		if keywords:
			keywords = keywords.replace("keywords = ", '')
		if description:
			description = description.replace("description = ", '')

		[divs.extract() for divs in html.body.findAll('div')]
		body = html.body.renderContents()
		style = html.style.prettify()

		result = {
			'entry': entry,
			'title': title,
			'html': html,
			'body': body.replace('http:///', '/'),
			'style': style,
			'id': id,
			'head_title': head_title,
			'keywords': keywords,
			'description': description,
			}
		if use_cache:
			memcache.add(id, result)
	return result


def _get_doc_id_by_q(q):
	q = q.encode('UTF-8')
	result = None
	if googleUsers.is_current_user_admin():
		memcache.delete(q)
	else:
		result = memcache.get(q)
	if not result:
		uri = '/feeds/default/private/full?title=%s&title-exact=true&max-results=1&showfolders=false' % q
		feeds = get_doc_list(uri)
		print feeds
		for doc in feeds.entry:
			folders = doc.InFolders()
			document_type = doc.GetDocumentType()
			result = {
				'type': document_type,
				'is_folder': (document_type == 'folder'),
				'is_document': (document_type == 'document'),
				'id': doc.resource_id.text.replace(document_type + ':', ''),
				'full_id': doc.resource_id.text,
				'folders': folders,
			  'item':doc,
				}
			memcache.set(q, result)

	return result


def get_doc_list(uri):
	client = init_gdata_client()
	feeds = client.GetDocList(uri=uri)
	return feeds


def get_exported_gdoc(id):
	client = init_gdata_client()
	entry = client.GetFileContent('/feeds/download/documents/Export?id=%s&format=html' % id)
	return entry


client = None

def init_gdata_client():
	global client, _get_doc_id_by_q
	if not client:
		client = gdata.docs.client.DocsClient(source='yourCo-yourAppName-v1')
		client.ssl = True # Force all API requests through HTTPS
		client.http_client.debug = True # Set to True for debugging HTTP requests
		client.ClientLogin(settings.DOCS_EMAIL, settings.DOCS_PASS, client.source)
	return client


def login(request):
	return HttpResponseRedirect(redirect_to=googleUsers.create_login_url(request.META['HTTP_REFERER']))


def logout(request):
	return HttpResponseRedirect(redirect_to=googleUsers.create_logout_url(request.META['HTTP_REFERER']))