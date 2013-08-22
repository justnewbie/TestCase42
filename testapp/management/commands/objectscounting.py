from django.core.management.base import BaseCommand
from django.db.models import get_app, get_models


class Command(BaseCommand):
    help = 'Show all models in app and count objects for each of them'

    def handle(self, *args, **options):
        app = get_app('testapp')
        for model in get_models(app):
            print('In model "{1}" is {0} objects.'.format(model.objects.count(), model._meta.object_name))
            self.stderr.write('{2} In model "{1}" is {0} objects.'.format(model.objects.count(),
                                                                          model._meta.object_name, 'error:'))
