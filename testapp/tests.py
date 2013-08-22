import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from models import Person


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


class ModelsTest(TestCase):
    def test_models(self):
        Person(first_name="Lara", last_name="Croft",
               about="I am the TOMB RIDER",
               b_date=datetime.datetime.now().date(),
               jabber="TombRider@world.m",
               email="TombRider@world.m").save()
