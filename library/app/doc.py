__author__ = 'pivo'

from google.appengine.api import memcache
from google.appengine.api import users as googleUser
from django.conf import settings
from library.system.BeautifulSoup import BeautifulStoneSoup
import gdata.docs.data
import gdata.docs.client
from application.main.models import *


class doc():
	@staticmethod
	def get_doc_q(q):
		q = q.encode('UTF-8')
		if googleUser.is_current_user_admin():
			memcache.delete(q)

		resource_id = memcache.get(q)
		if not resource_id:
			client = gdata.docs.client.DocsClient(source='yourCo-yourAppName-v1')
			client.ssl = True # Force all API requests through HTTPS
			client.http_client.debug = True # Set to True for debugging HTTP requests
			client.ClientLogin(settings.DOCS_EMAIL, settings.DOCS_PASS, client.source)
			feeds = client.GetDocList(
				uri='/feeds/default/private/full?title=%s&title-exact=true&max-results=1&showfolders=true' % q)
			for document in feeds.entry:
				resource_id = document.resource_id.text
				memcache.add(q, resource_id)
				return doc.get_doc(resource_id.replace('document:', ''))
		else:
			return doc.get_doc(resource_id.replace('document:', ''))
		return False

	@staticmethod
	def get_title(id):
		client = gdata.docs.client.DocsClient(source='yourCo-yourAppName-v1')
		client.ssl = True # Force all API requests through HTTPS
		client.http_client.debug = True # Set to True for debugging HTTP requests
		client.ClientLogin(settings.DOCS_EMAIL, settings.DOCS_PASS, client.source)
		feeds = client.GetDocList(
			uri='/feeds/default/private/full?title=%s&title-exact=true&max-results=1&showfolders=true' % q)
		for document in feeds.entry:
			resource_id = document.title.text

	@staticmethod
	def get_doc(id):
		if googleUser.is_current_user_admin():
			memcache.delete(id)

		entry = memcache.get(id)
		if not entry:
			client = gdata.docs.client.DocsClient(source='yourCo-yourAppName-v1')
			client.ssl = True # Force all API requests through HTTPS
			client.http_client.debug = True # Set to True for debugging HTTP requests
			client.ClientLogin(settings.DOCS_EMAIL, settings.DOCS_PASS, client.source)

			entry = client.GetFileContent(
				'/feeds/download/documents/Export?id=%s&format=html' % id)
			memcache.add(id, entry)
		html = BeautifulStoneSoup(entry, convertEntities=BeautifulStoneSoup.HTML_ENTITIES)
		body = html.body.renderContents()
		style = html.style.prettify()
		return {
			'entry': entry,
			'title': html.head.title.text,
			'html': html,
			'body': body.replace('http:///', '/'),
			'style': style,
			'id': id,
			}

	@staticmethod
	def set_root(id):
		key = settings.ROOT_KEY_DB_MEMCACHE
		memcache.set(key, id)
		root_page = PageDocs(title='')
		pass

