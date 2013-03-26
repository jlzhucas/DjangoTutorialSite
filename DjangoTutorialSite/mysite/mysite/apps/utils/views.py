# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.utils import simplejson



class AjaxResponseMixin(object):
    ''' Ajax response Mixin, return JSON data. '''

    def dumps(self, data):
        return simplejson.dumps(data)

    def render_to_json(self, context):
        return HttpResponse(self.dumps(context),
                            content_type='application/json')

    def ajax_response(self, context=None, **kwargs):
        if context is None:
            context = {}
        context.update(kwargs)
        return self.render_to_json(context)
