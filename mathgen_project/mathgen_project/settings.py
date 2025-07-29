import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'fake-key'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = ['genealogy', 'django.contrib.staticfiles']
MIDDLEWARE = ['django.middleware.common.CommonMiddleware']
ROOT_URLCONF = 'mathgen_project.urls'
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'genealogy', 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {},
}]
WSGI_APPLICATION = 'mathgen_project.wsgi.application'
STATIC_URL = '/static/'