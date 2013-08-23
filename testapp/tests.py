import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test.client import RequestFactory
from middlewares import RequestSaverMiddleware
from models import Person, RequestLogs
from testingslow import settings


class JsonDataTest(TestCase):
    def test_json_data(self):
        self.assertTrue(User.objects.get(pk=1))
        self.assertTrue(Person.objects.get(pk=1))


class ViewsTest(TestCase):
    def test_main_page(self):
        for field in Person._meta.fields:
            if field.name == 'id' or field.name == 'b_date':
                pass
            else:
                self.assertContains(self.client.get(reverse('main_page')),
                                    field.value_from_object(
                                        Person.objects.get(pk=1)))

    def test_requests_page(self):
        response = self.client.get(reverse('http_loggs_list'))
        self.assertContains(
            response, '<meta name="description" content="Last requests" />')
        self.assertContains(response, reverse('http_loggs_list'))


class ModelsTest(TestCase):
    def test_models(self):
        Person(first_name="Lara", last_name="Croft",
               about="I am the TOMB RIDER",
               b_date=datetime.datetime.now().date(),
               jabber="TombRider@world.m",
               email="TombRider@world.m").save()
        RequestLogs(url="/hooks/", method='GET',
                    time_stamp=datetime.datetime.now()).save()


class MiddlewareTest(TestCase):
    def test_hooks_middleware(self):
        RequestSaverMiddleware().process_request(
            RequestFactory().get(reverse('http_loggs_list')))
        self.assertEqual(reverse('http_loggs_list'),
                         RequestLogs.objects.get(pk=1).url)


class ContextProcessorTest(TestCase):
    def test_settings_processor(self):
        self.assertEquals(self.client.get(reverse('main_page')).context['settings'].ROOT_URLCONF, settings.ROOT_URLCONF)
