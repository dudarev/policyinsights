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

## Enabling Sendgrid

```
heroku addons:create sendgrid:starter
heroku config:get SENDGRID_USERNAME
heroku config:get SENDGRID_PASSWORD
```

## Reset database

```
heroku pg:reset DATABASE_URL
```

## Database backups

https://devcenter.heroku.com/articles/heroku-postgres-backups