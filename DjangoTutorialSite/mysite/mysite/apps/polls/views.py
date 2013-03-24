from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import TemplateView

from mysite.apps.polls.models import Poll, Choice


class IndexView(TemplateView):
    ''' Index page view. '''

    template_name = "polls/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        latest_poll_list = Poll.objects.all().order_by('-pub_date')
        context.update({'latest_poll_list': latest_poll_list})
        return context
        

class DetailView(TemplateView):
    ''' Poll detail page view. '''

    template_name = "polls/detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        poll_id = kwargs.get("poll_id", None) 
        p = get_object_or_404(Poll, pk=poll_id)
        context.update({"poll": p})
        return context


class ResultsView(TemplateView):
    ''' Poll results page view. '''

    template_name = "polls/results.html"

    def get_context_data(self, **kwargs):
        context = super(ResultsView, self).get_context_data(**kwargs)
        poll_id = kwargs.get("poll_id", None)
        p = get_object_or_404(Poll, pk=poll_id)
        context.update({"poll": p})
        return context


class VoteView(TemplateView):
    ''' Poll vote page view. '''
    
    template_name = "polls/detail.html"

    def get(self, request, *args, **kwargs):
        poll_id = kwargs.get("poll_id", None)
        p = get_object_or_404(Poll, pk=poll_id)
        context = self.get_context_data(**kwargs)
        context.update({"poll": p})
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        poll_id = kwargs.get("poll_id", None)
        p = get_object_or_404(Poll, pk=poll_id)
        context = self.get_context_data(**kwargs)
        try:
            selected_choice = p.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            context.update({
                "poll": p,
                "error_message": "You did not select a choice."
            })
            return self.render_to_response(context)
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('detail', args=(p.id, )))

