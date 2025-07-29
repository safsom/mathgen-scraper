
SECRET_KEY = 'dev'
DEBUG = True
ROOT_URLCONF = 'mathgen_project.urls'
INSTALLED_APPS = ['mathgen']
ALLOWED_HOSTS = ['*']
MIDDLEWARE = []
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': []},
}]
