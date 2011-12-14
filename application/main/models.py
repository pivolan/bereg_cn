from google.appengine.ext import db
from django.contrib.auth import authenticate, login, logout
from django.contrib.syndication.feeds import Feed
from google.appengine.api import images
from google.appengine.api import users as googleUsers

#from appengine_admin.db_extensions import ManyToManyProperty

from django import forms
from django.utils.translation import ugettext as _

class Users(db.Model):
	uid = db.UserProperty()
	name = db.StringProperty()
	fio = db.StringProperty()
	company = db.StringProperty()
	phone = db.StringProperty()
	address = db.StringProperty()

	def email(self):
		return self.uid.email()

	def nickname(self):
		return self.uid.nickname()

	def user_id(self):
		return self.uid.user_id()

	def federated_identity(self):
		return self.uid.federated_identity()

	def federated_provider(self):
		return self.uid.federated_provider()

	def is_current_user_admin(self):
		return googleUsers.is_current_user_admin()


class Seo(db.Model):
	description = db.StringProperty()
	meta = db.StringListProperty()
	keywords = db.StringListProperty()


class EasyPage(db.Model):
	title = db.StringProperty(required=True)
	content = db.TextProperty(required=True)
	seo = db.ReferenceProperty(Seo, collection_name='easyPages')


class PageDocs(db.Model):
	title = db.StringProperty(required=True)
	seo = db.ReferenceProperty(Seo, collection_name='PageDocs')
	father = db.SelfReferenceProperty(collection_name='children')