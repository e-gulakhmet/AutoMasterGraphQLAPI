from .common import *

DEBUG = False

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
SECURE_AUTH_SALT = os.environ.get('SECURE_AUTH_SALT')

BASE_URL = os.environ.get('BASE_URL')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')


STATIC_URL = '/static/'
MEDIA_PATH = 'media'
MEDIA_URL = '%s/%s/' % (BASE_URL, MEDIA_PATH)
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
