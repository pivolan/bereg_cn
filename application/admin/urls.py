from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns("",
	(r"^add$", "application.admin.views.add"),
	(r"^remove$", "application.admin.views.remove"),
	(r"^test$", "application.admin.views.test"),
	(r"^login$", "application.admin.views.login"),
	(r"^logout$", "application.admin.views.logout"),

	(r"^clear_cache", "application.admin.views.clear_cache"),

	(r"^docstree$", "application.admin.views.docstree"),
	(r"^docstree/(.*)$", "application.admin.views.docstree"),
                       
	(r"^(.*)$", "application.admin.views.index"),


#	(r"^test/*$", "application.admin.views.test"),
#	(r"^uf$", "application.admin.views.formuser"),
#	(r"^form/(?P<newId>\d*)$", "application.admin.views.form"),
#	(r"^tree/(?P<kurator>\d*)$", "application.admin.views.tree"),
#
#	(r"^.*_eng.html$", "application.admin.views.eng"),
#	(r"^r(?P<refurl>\d+)$", "application.admin.views.index"),
#	(r"^index.html$", "application.admin.views.index"),
#	(r"^logout/$", "application.admin.views.logout_view"),
#	(r"^registration.html$", "application.admin.views.register"),
#	(r"^restorepassword.html$", "application.admin.views.restorepassword"),
#	(r"^new/(?P<id>\d+)$", "application.admin.views.news"),
#	(r"^(?P<name>[\w\-_]+).html$", "application.admin.views.pages"),
#	(r"^user/profile.html$", "application.admin.views.user_profile"),
#	(r"^user/profile.html/(?P<success>success)$", "application.admin.views.user_profile"),
#	(r"^user/status.html$", "application.admin.views.user_status"),
#	(r"^user/partners.html$", "application.admin.views.user_partners"),
#	(r"^user/books1.html$", "application.admin.views.user_books1"),
#	(r"^user/books2.html$", "application.admin.views.user_books2"),
#	(r"^user/ajax/order.html$", "application.admin.views.user_order"),
#	(r"^user/order.html$", "application.admin.views.user_order"),
#	(r"^user/order.html/(?P<image>\d+)$", "application.admin.views.user_order"),
#	(r"^user/partner/(?P<member>\d+)$", "application.admin.views.user_partners"),
#	(r"^user/delete/(?P<partnerId>\d+)$", "application.admin.views.user_delete_partner"),
#	(r"^user/mail.html$", "application.admin.views.user_mail"),
#	(r"^user/activate/(?P<level>\d*)$", "application.admin.views.user_activate"),
#	(r"^user/activated/(?P<level>\d*)$", "application.admin.views.user_activated"),
#	(r"^user/mail/$", "application.admin.views.user_mail"),
#	(r"^user/news/*$", "application.admin.views.user_news"),
#	(r"^user/mail/id(?P<id>\d+)$", "application.admin.views.user_mail_show"),
#	(r"^user/mail/out/*$", "application.admin.views.user_mail_out"),
#	(r"^user/sentmail/(?P<id>\d*)$", "application.admin.views.user_sentmail"),
#	(r"^user/(?P<page>\w+).html$", "application.admin.views.user"),
#	(r"^user/$", "application.admin.views.user_status"),
#	(r"^tasks/summary/$", "application.admin.views.tasks_summary"),
#	(r"^admin/edit/(?P<userId>\d+)$", "application.admin.views.adminEdit"),
#	(r"^admin/(?P<key>\w*)$", "application.admin.views.admin"),
#	(r"^flush/*$", "application.admin.views.flush"),
#	(r"^blob/(?P<id>\d*)$", "application.admin.views.blob"),
#                       #cron jobs update admin stat
#	(r"^cronjobs$", "application.admin.views.cron_jobs"),
#
#	(r"^.*$", "application.admin.views.eng"),
)