from django.contrib import admin
from models import Person


class PersonAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'b_date',
              'about', 'email', 'jabber')
    list_display = ('first_name', 'last_name')

admin.site.register(Person, PersonAdmin)
