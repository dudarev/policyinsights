dump_test_data:
	./manage.py dumpdata --indent=2 locations > locations/fixtures/locations_test_data.json
	./manage.py dumpdata --indent=2 programs > programs/fixtures/programs_test_data.json

load_test_data_heroku:
	heroku run python manage.py loaddata locations_test_data
	heroku run python manage.py loaddata programs_test_data

load_sites:
	heroku run python manage.py loaddata sites

migrate_heroku:
	heroku run python manage.py migrate

# reset_interventions_heroku:
# 	heroku run python manage.py migrate interventions zero
# 	heroku run python manage.py migrate
