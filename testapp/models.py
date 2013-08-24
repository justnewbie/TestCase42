from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    b_date = models.DateField()
    about = models.CharField(max_length=500)
    email = models.EmailField(max_length=50, blank=True, unique=True)
    jabber = models.CharField(max_length=20)
    photography = models.ImageField(upload_to="images", default='images/test.jpg')

    def __unicode__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class RequestLogs(models.Model):
    url = models.CharField(max_length=500)
    method = models.CharField(max_length=5)
    time_stamp = models.DateField()

    def __unicode__(self):
        return self.http_request
