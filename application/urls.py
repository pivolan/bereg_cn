from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns("",
	(r"^$", "application.main.controllers.index.index"),
	(r"^page/(\d*)$", "application.main.controllers.index.index"),
	(r"^login$", "application.main.controllers.index.login"),
	(r"^logout$", "application.main.controllers.index.logout"),
	(r"^admin/", include("application.admin.urls")),

#	(r"^test/*$", "application.main.views.test"),
#	(r"^uf$", "application.main.views.formuser"),
#	(r"^form/(?P<newId>\d*)$", "application.main.views.form"),
#	(r"^tree/(?P<kurator>\d*)$", "application.main.views.tree"),
#
#	(r"^.*_eng.html$", "application.main.views.eng"),
#	(r"^r(?P<refurl>\d+)$", "application.main.views.index"),
#	(r"^index.html$", "application.main.views.index"),
#	(r"^logout/$", "application.main.views.logout_view"),
#	(r"^registration.html$", "application.main.views.register"),
#	(r"^restorepassword.html$", "application.main.views.restorepassword"),
#	(r"^new/(?P<id>\d+)$", "application.main.views.news"),
#	(r"^(?P<name>[\w\-_]+).html$", "application.main.views.pages"),
#	(r"^user/profile.html$", "application.main.views.user_profile"),
#	(r"^user/profile.html/(?P<success>success)$", "application.main.views.user_profile"),
#	(r"^user/status.html$", "application.main.views.user_status"),
#	(r"^user/partners.html$", "application.main.views.user_partners"),
#	(r"^user/books1.html$", "application.main.views.user_books1"),
#	(r"^user/books2.html$", "application.main.views.user_books2"),
#	(r"^user/ajax/order.html$", "application.main.views.user_order"),
#	(r"^user/order.html$", "application.main.views.user_order"),
#	(r"^user/order.html/(?P<image>\d+)$", "application.main.views.user_order"),
#	(r"^user/partner/(?P<member>\d+)$", "application.main.views.user_partners"),
#	(r"^user/delete/(?P<partnerId>\d+)$", "application.main.views.user_delete_partner"),
#	(r"^user/mail.html$", "application.main.views.user_mail"),
#	(r"^user/activate/(?P<level>\d*)$", "application.main.views.user_activate"),
#	(r"^user/activated/(?P<level>\d*)$", "application.main.views.user_activated"),
#	(r"^user/mail/$", "application.main.views.user_mail"),
#	(r"^user/news/*$", "application.main.views.user_news"),
#	(r"^user/mail/id(?P<id>\d+)$", "application.main.views.user_mail_show"),
#	(r"^user/mail/out/*$", "application.main.views.user_mail_out"),
#	(r"^user/sentmail/(?P<id>\d*)$", "application.main.views.user_sentmail"),
#	(r"^user/(?P<page>\w+).html$", "application.main.views.user"),
#	(r"^user/$", "application.main.views.user_status"),
#	(r"^tasks/summary/$", "application.main.views.tasks_summary"),
#	(r"^admin/edit/(?P<userId>\d+)$", "application.main.views.adminEdit"),
#	(r"^admin/(?P<key>\w*)$", "application.main.views.admin"),
#	(r"^flush/*$", "application.main.views.flush"),
#	(r"^blob/(?P<id>\d*)$", "application.main.views.blob"),
#                       #cron jobs update main stat
#	(r"^cronjobs$", "application.main.views.cron_jobs"),
#
#	(r"^.*$", "application.main.views.eng"),
)