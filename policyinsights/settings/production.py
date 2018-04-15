from .heroku import *

from os import getenv


SITE_ID = getenv('SITE_ID', SITE_ID)
