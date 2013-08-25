from django.contrib import admin

from models import Person, RequestLogs


class PersonAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'b_date',
              'about', 'email', 'jabber')
    list_display = ('first_name', 'last_name')

admin.site.register(Person, PersonAdmin)


class RequestLogsAdmin(admin.ModelAdmin):
    fields = ('url', 'method', 'time_stamp')
    list_display = ('url',)

admin.site.register(RequestLogs, RequestLogsAdmin)
