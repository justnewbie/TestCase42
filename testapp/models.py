from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    b_date = models.DateField()
    about = models.CharField(max_length=500)
    email = models.EmailField(max_length=50, blank=True, unique=True)
    jabber = models.CharField(max_length=20)

    def __unicode__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Hook_http(models.Model):
    http_request = models.CharField(max_length=500)

    def __unicode__(self):
        return '{0}'.format(self.http_request)