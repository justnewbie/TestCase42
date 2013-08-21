"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import datetime
from django.test import TestCase, Client
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from django.template import Template
from django.template import Context
from models import Person, Hook_http
from testingslow import settings


class JsonDataTest(TestCase):
    def test_json_data(self):
        print('User "{0}" and profile "{1}" was  successfully CREATED;'.format(User.objects.get(pk=1),
                                                                               Person.objects.get(pk=1)))


class ViewsTest(TestCase):
    def test_main_page(self):
        c = Client()
        response = c.get('/')
        self.assertContains(response, '<meta name="description" content="Main Page" />')

    def test_hooks_page(self):
        c = Client()
        response = c.get('/hooks/')
        self.assertContains(response, '<meta name="description" content="Last requests" />')
        self.assertContains(response, 'http://testserver/')


class ModelsTest(TestCase):
    def test_models(self):
        Person(first_name="Lara", last_name="Croft", about="I am the TOMB RIDER",
               b_date=datetime.datetime.now().date(), jabber="TombRider@world.m",
               email="TombRider@world.m").save()
        Hook_http(http_request="http://testserver/").save()


class MiddlewareTest(TestCase):
    def test_hooks_middleware(self):
        c = Client()
        response = c.get('/')
        print('Request to "{0}" is successfully SAVED;'.format(Hook_http.objects.get(pk=1)))


class ContextProcessorTest(TestCase):
    def test_settings_processor(self):
        c = Client()
        self.assertEquals(c.get('/').context['settings'].ROOT_URLCONF, settings.ROOT_URLCONF)