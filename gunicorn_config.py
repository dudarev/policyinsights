# based on https://medium.com/@bfirsh/squeezing-every-drop-of-performance-out-of-a-django-app-on-heroku-4b5b1e5a3d44
# https://github.com/jneight/django-db-geventpool
from psycogreen.gevent import patch_psycopg     # use this if you use gevent workers


def post_fork(server, worker):
    patch_psycopg()
    worker.log.info("Made Psycopg2 Green")