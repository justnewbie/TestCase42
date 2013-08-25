test:
	python $(PWD)/manage.py test testapp
run:
	python $(PWD)/manage.py runserver
syncdb:
	python $(PWD)/manage.py syncdb --no-initial-data --noinput
	python $(PWD)/manage.py migrate