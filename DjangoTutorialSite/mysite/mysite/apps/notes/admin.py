# -*- coding: utf-8 -*-
from django.contrib import admin
from mysite.apps.notes.models import Note

class NoteAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']

admin.site.register(Note, NoteAdmin)
