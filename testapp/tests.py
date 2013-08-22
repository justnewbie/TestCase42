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
        #testing auth form
        self.assertContains(response, 'Login form')
        self.assertNotContains(response, '<p>You are logged in...</p>')
        c.post('/login/', {'username': 'admin', 'password': 'admin'})
        response = c.get('/')
        self.assertContains(response, '<p>You are logged in...</p>')
        self.assertNotContains(response, 'Login form')

    def test_hooks_page(self):
        c = Client()
        response = c.get('/hooks/')
        self.assertContains(response, '<meta name="description" content="Last requests" />')
        self.assertContains(response, 'http://testserver/')

    def test_manage_page(self):
        c = Client()
        # testing login required
        response = c.get('/manage/?person=1')
        self.assertEqual(response.status_code, 302)
        # testing login view
        response = c.post('/login/', {'username': 'admin', 'password': 'admin'})
        # testing manage view
        response = c.get('/manage/?person=1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<meta name="description" content="Manage Main Page" />')
        with open(settings.MEDIA_ROOT+'/images/test.jpg') as fp:
            response = c.post('/manage/?person=1', {'first_name': 'Lara', 'last_name': 'Croft',
                                                    'b_date': datetime.datetime.now().date(),
                                                    'about': 'I am the tomb rider', 'jabber': 'L_Croft',
                                                    'email': 'Croft@i.ua',
                                                    'photography': fp})
            self.assertContains(response, 'Data saved')
        # testing logout view
        response = c.post('/loggout/')
        response = c.get('/manage/?person=1')
        self.assertEqual(response.status_code, 302)


class ModelsTest(TestCase):
    def test_models(self):
        Person(first_name="Lara", last_name="Croft", about="I am the TOMB RIDER",
               b_date=datetime.datetime.now().date(), jabber="TombRider@world.m",
               email="TombRider@world.m", photography='images/test.jpg').save()
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