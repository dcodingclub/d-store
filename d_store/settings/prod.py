import os
from .common import *

SECRET_KEY = os.environ('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["dcodingclub.space"]