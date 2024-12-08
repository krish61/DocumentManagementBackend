:PHONY:=run migrate shell
:DEFAULT:= run
run:
	@python manage.py runserver
migrate:
	@python manage.py makemigrations && python manage.py migrate
shell:
	@python manage.py shell
test:
	@coverage run manage.py test --keepdb -v2
