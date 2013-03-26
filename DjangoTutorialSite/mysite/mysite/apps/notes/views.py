# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.views.generic import CreateView
from django.views.generic import DetailView 
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import View
# from django.utils import simplejson

from mysite.apps.notes.models import Note
from mysite.apps.utils.views import AjaxResponseMixin


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

    http_method_names = ['post', ]
    
    @login_required
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

    http_method_names = ['post', ]

    @login_required
    def post(self, request, *args, **kwargs):
        post_data = request.POST.copy()
        slug = kwargs.get('slug', '')
        note = Note.objects.get(slug=slug)
        if post_data.has_key('slug'):
            slug_str = post_data['slug']
            if note.slug != slug_str:
                try:
                    Note.objects.get(slug=slug_str)
                    error_msg = u"Slug already taken. "
                    return HttpResponseServerError(error_msg)
                except Note.DoesNotExist:
                    note.slug = slug_str
        if post_data.has_key('title'):
            note.title = post_data['title']
        if post_data.has_key('text'):
            note.text = post_data['text']
        note.save()
        return HttpResponseRedirect(note.get_absolute_url())


class AjaxCreateNoteView(View, AjaxResponseMixin):
    ''' Ajax create note page view. '''

    http_method_names = ['post', ]

    # @login_required
    def post(self, request, *args, **kwargs):
        context = {}
        post_data = request.POST.copy()
        if post_data.has_key('slug') and post_data.has_key('title'):
            slug = post_data['slug']
            try:
                note = Note.objects.get(slug=slug)
                context.update({
                    'msg': u"Slug already taken. ", 
                    'slug': note.slug
                })
                return self.ajax_response(context)
            except Note.DoesNotExist:
                title = post_data['title']
                note = Note.objects.create(title=title, slug=slug)
                context.update({
                    'msg': u"Create note successfully!",
                    'title': title,
                    'slug': slug,
                    'url': note.get_absolute_url()
                })
                return self.ajax_response(context)
        else:
            context.update({'msg': u"Insufficient POST data"})
            return self.ajax_response(context)

class AjaxUpdateNoteView(View, AjaxResponseMixin):
    ''' Ajax update note page view. '''

    http_method_names = ['post', ]

    # @login_required
    def post(self, request, *args, **kwargs):
        context = {}
        post_data = request.POST.copy()
        slug = kwargs.get('slug', '')
        note = Note.objects.get(slug=slug)
        if post_data.has_key('slug'):
            slug_str = post_data['slug']
            if note.slug != slug_str:
                try:
                    Note.objects.get(slug=slug_str)
                    context.update({
                        'msg': u"Slug '%s' already taken. "% slug_str, 
                        'slug': note.slug
                    })
                    return self.ajax_response(context)
                except Note.DoesNotExist:
                    note.slug = slug_str
                    context.update({'url': note.get_absolute_url()})
        if post_data.has_key('title'):
            note.title = post_data['title']
        if post_data.has_key('text'):
            note.text = post_data['text']
        note.save()
        context.update({'msg': 'Update successfully!'})
        return self.ajax_response(context)


class AjaxSlugVerifyView(View):
    ''' Ajax verify the slug. '''

    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        get_data = request.GET.copy()
        if get_data.has_key('slug'):
            slug_str = get_data['slug']
            try:
                Note.objects.get(slug=slug_str)
                return HttpResponseServerError(slug_str)
            except Note.DoesNotExist:
                return HttpResponse(slug_str)
