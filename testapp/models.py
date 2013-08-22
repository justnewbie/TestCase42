import datetime
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    b_date = models.DateField()
    about = models.CharField(max_length=500)
    email = models.EmailField(max_length=50, blank=True, unique=True)
    jabber = models.CharField(max_length=20)
    photography = models.ImageField(upload_to="images")

    def __unicode__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Hook_http(models.Model):
    http_request = models.CharField(max_length=500)

    def __unicode__(self):
        return '{0}'.format(self.http_request)


class Loggs(models.Model):
    action = models.CharField(max_length=15)
    date = models.DateField()
    table = models.CharField(max_length=30)

    def __unicode__(self):
        return '{0} {1}'.format(self.table, self.action)


@receiver(pre_save, sender=Hook_http)
@receiver(pre_save, sender=Person)
def saver_modifier(sender, **kwargs):
    try:
        Loggs(action='Modified', date=datetime.datetime.now().date(),
              table=sender.objects.get(id=kwargs['instance'].pk)._meta.object_name).save()
    except:
        Loggs(action='Created', date=datetime.datetime.now().date(),
              table=kwargs['instance']._meta.object_name).save()


@receiver(pre_delete, sender=Hook_http)
@receiver(pre_delete, sender=Person)
def deleter(sender, **kwargs):
    Loggs(action='Delete', date=datetime.datetime.now().date(),
          table=kwargs['instance']._meta.object_name).save()





















