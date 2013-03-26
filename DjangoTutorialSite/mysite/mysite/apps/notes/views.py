# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.views.generic import ListView
from django.views.generic import DetailView 
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.utils import simplejson as json

from mysite.apps.notes.models import Note


class NoteListView(ListView):
    ''' Note list page view. '''

    model = Note
    template_name = "notes/note_list.html"
    context_object_name = "notes"
    

class NoteDetailView(DetailView):
    ''' Note detail page view. '''

    model = Note
    template_name = "notes/note_detail.html"
    context_object_name = "note"



class CreateNoteView(CreateView):
    ''' Create note page view. '''

    http_method_names = [u'post', ]
    
    def post(self, request, *args, **kwargs):
        post_data = request.POST.copy()
        if post_data.has_key('slug') and post_data.has_key('title'):
            slug = post_data['slug']
            try:
                note = Note.objects.get(slug=slug)
                error_msg = u"Slug already in use."
            except Note.DoesNotExist:
                title = post_data['title']
                note = Note.objects.create(title=title, slug=slug)
                return HttpResponseRedirect(note.get_absolute_url())
        else:
            error_msg = u"Insufficient POST data"
        return HttpResponseServerError(error_msg)


class UpdateNoteView(UpdateView):
    ''' Update note page view. '''

    http_method_names = [u'post', ]

    def post(self, request, *args, **kwargs):
        post_data = request.POST.copy()
        slug = kwargs.get('slug', '')
        note = Note.objects.get(slug=slug)
        if post_data.has_key('slug'):
            slug_str = post_data['slug']
            if note.slug != slug_str:
                try:
                    n = Note.objects.get(slug=slug_str)
                    response = {'msg': u"Slug already taken. ", 'slug': note.slug}
                    return HttpResponse(json.dumps(response))
                except Note.DoesNotExist:
                    note.slug = slug_str
        if post_data.has_key('title'):
            note.title = post_data['title']
        if post_data.has_key('text'):
            note.text = post_data['text']
        note.save()
        response = {'msg': 'Update successfully!'}
        return HttpResponse(json.dumps(response))



