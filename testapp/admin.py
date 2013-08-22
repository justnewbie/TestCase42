from django.contrib import admin
from models import Person, Hook_http


class PersonAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'b_date', 'about', 'email', 'jabber', 'photography')
    list_display = ('first_name', 'last_name')
admin.site.register(Person, PersonAdmin)


class HookAdmin(admin.ModelAdmin):
    fields = ('http_request',)
    list_display = ('http_request',)
admin.site.register(Hook_http, HookAdmin)