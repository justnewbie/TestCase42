from django import template
from django.core import urlresolvers


register = template.Library()


def admin_link(self):
    return urlresolvers.reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.module_name), args=(self.id,))

register.simple_tag(admin_link)