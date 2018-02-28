## JS Libraries for Plots

Possible good JS-libraries for showing plots:

- http://c3js.org/ - may load from CSV
- http://www.chartjs.org/ - loads from JSON


## USAspending.gov source code

### Frontend

Frontend is provided

https://github.com/fedspendingtransparency/usaspending-website

Counties data for frontend

https://github.com/fedspendingtransparency/usaspending-website/tree/dev/src/data/counties

### Backend

Backed is provided via API

https://github.com/fedspendingtransparency/usaspending-api

Locations related models:

https://github.com/fedspendingtransparency/usaspending-api/blob/dev/usaspending_api/references/models.py

API docs:

https://api.usaspending.gov/docs/endpoints
https://api.usaspending.gov/api/v1/references/locations/


## Serving static files with CDN

As the app growth, consider serving static assets from CND:

http://django-storages.readthedocs.io/en/latest/

## Markdow

https://github.com/neutronX/django-markdownx

## Input Data Sanitization

https://stackoverflow.com/questions/5641901/sanitizing-html-in-submitted-form-data

- bleach
- strip_tags
- escape

## Doing less than, greater than in Postgres

https://stackoverflow.com/questions/44531689/how-can-i-do-less-than-greater-than-in-json-postgres-fields
