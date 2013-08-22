# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token
from forms import Add_Person, AuthForm
from models import Person, Hook_http


def about_p(request):
    return render_to_response('main_page.html',
                              {'My': Person.objects.get(pk=1), 'form': AuthForm},
                              context_instance=RequestContext(request))


def list_hooks(request):
    return render_to_response('loggs.html',
                              {'hooks': Hook_http.objects.all()[:10], },
                              context_instance=RequestContext(request))


@login_required
def manage_p(request):
    if request.method == 'GET' and 'person' in request.GET:
        article = Person.objects.get(pk=request.GET['person'])
        form = Add_Person(instance=article)
        return render_to_response('m_person.html', {'form': form}, context_instance=RequestContext(request))
    if request.method == 'POST' and 'person' in request.GET:
        article = Person.objects.get(pk=request.GET['person'])
        form = Add_Person(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return HttpResponse('Data saved')
        else:
            return HttpResponse('Invalid Data')


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        return HttpResponse('Invalid Data')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')