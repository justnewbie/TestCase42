MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=testingslow.settings $(MANAGE) test	
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=testingslow.settings $(MANAGE) syncdb --noinput
run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=testingslow.settings $(MANAGE) runserver
syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=testingslow.settings $(MANAGE) syncdb --noinput
