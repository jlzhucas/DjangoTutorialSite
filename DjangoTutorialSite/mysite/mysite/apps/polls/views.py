from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from mysite.apps.polls.models import Poll, Choice


def index(request):
    template_name = "polls/index.html"
    latest_poll_list = Poll.objects.all().order_by('-pub_date')
    output = ', '.join([p.question for p in latest_poll_list])
    context = {'latest_poll_list': latest_poll_list}
    return render_to_response(template_name, context)


def detail(request, poll_id):
    template_name = "polls/detail.html"
#     try:
#         p = Poll.objects.get(pk=poll_id)
#     except Poll.DoesNotExist:
#         raise Http404
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response(template_name, {'poll': p})


def results(request, poll_id):
    template_name = "polls/results.html"
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response(template_name, {'poll': p})


def vote(request, poll_id):
    template_name = "polls/detail.html"
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render_to_response(template_name, {
            'poll': p,
            'error_message': "You did not select a choice."
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('detail', args=(p.id, )))
