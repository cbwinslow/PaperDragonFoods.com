# settings.py

...
INSTALLED_APPS = [
    ...
    'django.contrib.sessions',
]

MIDDLEWARE = [
    ...
    'django.middleware.csrf.CsrfViewMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Change to your preferred DBMS.
        'NAME': 'cbwhubdb',                        # Update database name and credentials.
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),  # Static file directory.
)

STATIC_URL = '/static/'
