# Heroku settings

## Pointing to settings file
```
heroku config:set DJANGO_SETTINGS_MODULE=policyinsights.settings.heroku
```

## Database migrations

```
heroku run python manage.py migrate
```

## Admin user creation
```
heroku run python manage.py createsuperuser
```