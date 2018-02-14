dump_test_data:
	./manage.py dumpdata --indent=2 interventions > interventions/fixtures/interventions_test_data.json

load_test_data_heroku:
	heroku run python manage.py loaddata interventions_test_data

migrate_heroku:
	heroku run python manage.py migrate

reset_interventions_heroku:
	heroku run python manage.py migrate interventions zero
	heroku run python manage.py migrate
