from StringIO import StringIO
import datetime
from django.db.models import get_app, get_models
from django.core.management import call_command
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import RequestContext
from django.test import TestCase

from middlewares import RequestSaverMiddleware
from templatetags.admin_link import admin_link
from models import Person, RequestLogs
from widgets import DatePickerWidget
from testingslow import settings


contact = {'first_name': 'Lara', 'last_name': 'Croft',
           'b_date': datetime.datetime.now().date(),
           'about': 'I am the tomb rider', 'jabber':
           'L_Croft', 'email': 'Croft@i.ua', }


class JsonDataTest(TestCase):
    def test_json_data(self):
        self.assertTrue(User.objects.get(pk=1))
        self.assertTrue(Person.objects.get(pk=1))


class ViewsTest(TestCase):
    def test_main_page(self):
        response = self.client.get(reverse('main_page'))
        for field in Person._meta.fields:
            if field.name == 'id' or field.name == 'b_date' or field.name == 'photography':
                pass
            else:
                self.assertContains(response,
                                    field.value_from_object(
                                        Person.objects.get(pk=1)))
        self.assertContains(response, 'Login')
        self.assertNotContains(response, 'LogOut')
        self.client.post(reverse('login_view'), {'username': 'admin', 'password': 'admin'})
        response = self.client.get(reverse('main_page'))
        self.assertContains(response, 'LogOut')
        self.assertNotContains(response, 'Login')

    def test_requests_page(self):
        response = self.client.get(reverse('http_loggs_list'))
        self.assertContains(
            response, '<meta name="description" content="Last requests" />')
        self.assertContains(response, reverse('http_loggs_list'))
        for request in RequestLogs.objects.all()[::-1][:10]:
            self.assertContains(response, request.url)

    def test_manage_page(self):
        # testing login required
        self.assertEqual(self.client.get(reverse('manage_main_page', args=[1])).status_code, 302)
        self.client.post(reverse('login_view'), {'username': 'admin', 'password': 'admin'})
        response = self.client.get(reverse('manage_main_page', args=[1]))
        for field in Person._meta.fields:
            if field.name == 'id' or field.name == 'b_date':
                pass
            else:
                self.assertContains(response,
                                    field.value_from_object(
                                        Person.objects.get(pk=1)))
        self.assertEqual(response.status_code, 200)
        # testing manage view
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, """<script>
            $(function() {
                var pickerOpts = {
                    dateFormat: "yy-mm-dd",
                    showOtherMonths: true}
                $(".datepicker").datepicker(pickerOpts);
            });</script>""")
        with open(settings.MEDIA_ROOT+'/images/test.jpg') as fp:
            contact.update({'photography': fp})
            response = self.client.post(reverse('manage_main_page', args=[1]), contact)
            self.assertContains(response, 'Data saved')
        # testing logout view
        self.client.post(reverse('logout_view'))
        self.assertEqual(self.client.get(reverse('manage_main_page', args=[1])).status_code, 302)


class ModelsTest(TestCase):
    def test_models(self):
        Person(photography='images/test.jpg', **contact).save()
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
        self.assertEqual(RequestContext(RequestFactory)['settings'], settings)
        self.assertTrue('testapp.context_processors.settings_processor'
                        in settings.TEMPLATE_CONTEXT_PROCESSORS)


class DateWidgetTest(TestCase):
    def test_date_widget(self):
        self.client.post(reverse('login_view'), {'username': 'admin', 'password': 'admin'})
        response = self.client.get(reverse('manage_main_page', args=[1]))
        self.assertTrue("""<script>
            $(function() {
                var pickerOpts = {
                    dateFormat: "yy-mm-dd",
                    showOtherMonths: true}
                $(".datepicker").datepicker(pickerOpts);
            });</script>
            <input id="id_test" name="test" class="datepicker" type="text" value="1989-07-07"/>""",
                        DatePickerWidget().render('test', "1989-07-07"))


class AdminTagTest(TestCase):
    def test_admin_tag(self):
        self.assertEqual(admin_link(User.objects.get(pk=1)), '/admin/auth/user/1/')


class CountCommandTest(TestCase):
    def test_objects_counting(self):
        data, errors = StringIO(), StringIO()
        call_command("objectscounting", stdout=data, stderr=errors)
        for model in get_models(get_app("testapp")):
            amount = str(model.objects.count())
            self.assertTrue(amount in data.getvalue() and amount in errors.getvalue()
                            and "error" in errors.getvalue())
            model = model._meta.object_name
            self.assertTrue(model in data.getvalue() and model in errors.getvalue())
