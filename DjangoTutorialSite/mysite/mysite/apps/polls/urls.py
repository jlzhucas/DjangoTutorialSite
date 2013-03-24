# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from mysite.apps.polls.views import IndexView
from mysite.apps.polls.views import DetailView
from mysite.apps.polls.views import ResultsView
from mysite.apps.polls.views import VoteView


urlpatterns = patterns('mysite.apps.polls.views',
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^(?P<poll_id>\d+)/$', DetailView.as_view(), name="detail"),
    url(r'^(?P<poll_id>\d+)/results/$', ResultsView.as_view(), name="results"),
    url(r'^(?P<poll_id>\d+)/vote/$', VoteView.as_view(), name="vote"),

)

