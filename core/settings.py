import os
from pathlib import Path

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Update these to match your conda env path!
CONDA_PREFIX = os.environ.get('CONDA_PREFIX', r'C:\Users\Lenovo\anaconda3\envs\tourista')

GDAL_LIBRARY_PATH = os.path.join(CONDA_PREFIX, 'Library', 'bin', 'gdal310.dll')
GEOS_LIBRARY_PATH = os.path.join(CONDA_PREFIX, 'Library', 'bin', 'geos_c.dll')
# (You can similarly point PROJ_LIB etc. if you run into missing‐CRS errors)

BASE_DIR = Path(__file__).resolve().parent.parent
GDAL_LIBRARY_PATH = r"C:\Users\Lenovo\Desktop\tourista_mvp\Backend\venv\Lib\site-packages\osgeo\gdal310.dll"
# Build paths inside the project like this: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-your-secret-key-here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.gis',
    'user_profiles',  # Changed from 'users'
    'trips',
    'local_businesses',
    'chatbot',
    'rest_framework',          # For API
    'frontend.apps.FrontendConfig',              # Your new frontend app
    'formtools',
    'widget_tweaks',
    # 'leaflet',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (34.0837, 74.7973),  # approximate center of Kashmir
    'DEFAULT_ZOOM': 8,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 18,
    'TILES': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
}

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Custom User Model
AUTH_USER_MODEL = 'user_profiles.CustomUser'
# AUTH_USER_MODEL = 'frontend.CustomUser'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
     {
         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
     },
     {
         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
     },
     {
         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
     },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login/Logout redirects
LOGIN_REDIRECT_URL = 'profile'
LOGOUT_REDIRECT_URL = 'home'

# Add these at the bottom
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend', 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


OSGEO4W = os.environ.get('OSGEO4W_ROOT', r'C:\OSGeo4W')
GDAL_LIBRARY_PATH = os.path.join(OSGEO4W, 'bin', 'gdal310.dll')
GEOS_LIBRARY_PATH = os.path.join(OSGEO4W, 'bin', 'geos_c.dll')


# optional, if you want a default
LOGOUT_REDIRECT_URL = 'landing'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JS, images shipped with your code)
STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / 'frontend' / 'static' ]
# In production, collectstatic will place files here:
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files (uploads by users)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEBUG = False
ALLOWED_HOSTS = ['*']  # for local testing
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')