from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from mysite.apps.polls.models import Poll


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
    return HttpResponse("You're looking at poll %s."% poll_id)


def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s."% poll_id)
