# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Person, RequestLogs


def about_p(request):
    return render_to_response('main_page.html',
                              {'My': Person.objects.get(pk=1), },
                              context_instance=RequestContext(request))


def list_request(request):
    return render_to_response('loggs.html',
                              {'requests': RequestLogs.objects.all()[:10], },
                              context_instance=RequestContext(request))
