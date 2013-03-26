# -*- coding: utf-8 -8-
from django.conf.urls.defaults import patterns, url
from mysite.apps.notes.views import NoteListView 
from mysite.apps.notes.views import NoteDetailView 
from mysite.apps.notes.views import CreateNoteView
from mysite.apps.notes.views import UpdateNoteView


urlpatterns = patterns('',
    url(r'^$', NoteListView.as_view(), name="note_list"),
    url(r'^note/(?P<slug>[-\w]+)/$', NoteDetailView.as_view(), name="note_detail"),
    url(r'^create/$', CreateNoteView.as_view(), name="create_note"),
    url(r'^note/(?P<slug>[-\w]+)/update/$', UpdateNoteView.as_view(), name="update_note"),
)

