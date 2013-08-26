# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson

from models import Person, RequestLogs
from forms import AddPersonForm


def about_p(request):
    return render_to_response('main_page.html',
                              {'My': Person.objects.get(pk=1), 'form': AuthenticationForm},
                              context_instance=RequestContext(request))


def list_request(request, url):
    if int(url) == 0:
        requests = RequestLogs.objects.all()[::-1][:10]
    else:
        requests = RequestLogs.objects.all()[:10]
    return render_to_response('loggs.html',
                              {'requests': requests, },
                              context_instance=RequestContext(request))


@login_required
def manage_p(request, url):
    article = Person.objects.get(pk=url)
    if request.method == 'GET':
        form = AddPersonForm(instance=article)
        return render_to_response('m_person.html', {'form': form}, context_instance=RequestContext(request))
    form = AddPersonForm(request.POST or None, request.FILES or None, instance=article)
    response = lambda data: HttpResponse(simplejson.dumps(data), mimetype="application/json")
    if form.is_valid():
        form.save()
        return response('Data saved')
    else:
        return response('Invalid data')
