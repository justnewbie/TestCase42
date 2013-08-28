from django.contrib import admin

from models import Person, RequestLogs, Loggs


class PersonAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'b_date',
              'about', 'email', 'jabber')
    list_display = ('first_name', 'last_name')

admin.site.register(Person, PersonAdmin)


class RequestLogsAdmin(admin.ModelAdmin):
    fields = ('url', 'method', 'time_stamp')
    list_display = ('url',)

admin.site.register(RequestLogs, RequestLogsAdmin)


class LoggsAdmin(admin.ModelAdmin):
    fields = ('action', 'date', 'table',)
    list_display = ('action', 'date', 'table',)

admin.site.register(Loggs, LoggsAdmin)
