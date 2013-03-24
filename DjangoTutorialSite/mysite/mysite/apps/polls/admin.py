# -*- coding: utf-8 -*-
from django.contrib import admin
from mysite.apps.polls.models import Poll, Choice


# class PollAdmin(admin.ModelAdmin):
#     list_display = ('question', 'pub_date', )
#     fields = ['pub_date', 'question']
# 
# admin.site.register(Poll, PollAdmin)
# 
# 
# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ('poll', 'choice', 'votes',)
#     search_fields = ('poll', 'choice', 'votes', ) 
#     fieldsets = [
#         (None, {'fields': ['poll']}),
#         ('Choice', {'fields': ['choice', 'votes']}),
#     ]
# 
# admin.site.register(Choice, ChoiceAdmin)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'was_published_recently')
    date_hierarchy = 'pub_date'
    fieldsets = [
        ('Question', {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline, ]

admin.site.register(Poll, PollAdmin)
