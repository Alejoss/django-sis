from __future__ import absolute_import
import os, sys, logging
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static_files/'),
    ('gumby_css', os.path.join(BASE_DIR, 'components/css/')),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
CKEDITOR_UPLOAD_PATH = os.path.join(BASE_DIR, 'media/uploads')
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components/')

LOGIN_REDIRECT_URL = "/"
MULTI_TENANT = os.getenv('MULTI_TENANT', False)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME', 'postgres'),
        'USER': os.getenv('DATABASE_USER', 'postgres'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_ADDR', 'db_1'),
        'PORT': 5432,
    }
}
EMAIL_HOST = 'daphne.cristoreyny.org'
# Prefered file format, may be changed in user preferences.
# Default o
# o = Open Document
# m = Microsoft Binary
# x = Microsoft XML
PREFERED_FORMAT = 'o'
TIME_ZONE = 'America/New_York'
TIME_INPUT_FORMATS = ('%I:%M %p', '%I:%M%p', '%H:%M:%S', '%H:%M')
TIME_FORMAT = 'h:i A'
DATE_INPUT_FORMATS = ('%m/%d/%Y', '%Y-%m-%d', '%m/%d/%y', '%b %d %Y',
'%b %d, %Y', '%d %b %Y', '%d %b, %Y', '%B %d %Y',
'%B %d, %Y', '%d %B %Y', '%d %B, %Y','%b. %d, %Y')
DATE_FORMAT = 'M j, Y'
BASE_URL = "http://localhost:8000"

# Global date validators, to help prevent data entry errors
import datetime
from django.core.validators import MinValueValidator # Could use MaxValueValidator too
DATE_VALIDATORS=[MinValueValidator(datetime.date(1970,1,1))] # Unix epoch!

USE_L10N = False
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'
LANGUAGES = (
  ('es', 'Spanish'),
  ('en', 'English'),
)
SITE_ID = 1
INTERNAL_IPS = ('127.0.0.1',)
USE_I18N = True
SECRET_KEY = '4@=mqjpx*f$3m(1-wl6&02p#cx@*dz4_t26lu@@pmd^2%+)**y'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'apptemplates.Loader',
    'django.template.loaders.eggs.Loader',
)
ROOT_URLCONF = 'django_sis.urls'
WSGI_APPLICATION = 'ecwsp.wsgi.application'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'ecwsp.sis.disable.DisableCSRF',
    )
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'ecwsp.sis.context_processors.global_stuff',
    'django.core.context_processors.static',
    'constance.context_processors.config',
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'compressor.finders.CompressorFinder',
)

DEBUG = True
TEMPLATE_DEBUG = True
AUTH_PROFILE_MODULE = 'sis.UserPreference'

#BOWER
BOWER_INSTALLED_APPS = (
    'jquery',
    'jquery-ui',
    'gumby',
    'jquery-migrate',
    'blockui',
    'jquery-color',
    'angular-route',
    'angular-ui-handsontable',
    'underscore',
    'restangular',
    'bootstrap-sass-official',
    'bootstrap-hover-dropdown',
    'angular-ui-bootstrap',
)

#GRAPPELLI
ADMIN_TOOLS_MENU = 'ecwsp.menu.CustomMenu'
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
GRAPPELLI_INDEX_DASHBOARD = 'ecwsp.dashboard.CustomIndexDashboard'
GRAPPELLI_ADMIN_TITLE = '<img src="/static/images/logo.png"/ style="height: 30px; margin-left: -10px; margin-top: -8px; margin-bottom: -11px;">'

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

#LDAP
LDAP = False
LDAP_SERVER = 'admin.example.org'
NT4_DOMAIN = 'ADMIN'
LDAP_PORT = 389
LDAP_URL = 'ldap://%s:%s' % (LDAP_SERVER, LDAP_PORT)
SEARCH_DN = 'DC=admin,DC=example,DC=org'
SEARCH_FIELDS = ['mail','givenName','sn','sAMAccountName','memberOf', 'cn']
BIND_USER = 'ldap'
BIND_PASSWORD = ''

#Google Apps
GAPPS = False
if GAPPS:
    GAPPS_DOMAIN = ''
    GAPPS_USERNAME = ''
    GAPPS_PASSWORD = ''
    GAPPS_ALWAY_ADD_GROUPS = False
    AUTHENTICATION_BACKENDS += ('ecwsp.google_auth.backends.GoogleAppsBackend',)

AUTHENTICATION_BACKENDS += ('django_su.backends.SuBackend',)

#CKEDITOR
CKEDITOR_MEDIA_PREFIX = "/static/ckeditor/"
CKEDITOR_UPLOAD_PATH = MEDIA_ROOT + "uploads"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            [ 'Bold', 'Italic', 'Underline', 'Subscript','Superscript',
              '-', 'Image', 'Link', 'Unlink', 'SpecialChar', 'equation',
              '-', 'Format',
              '-', 'Maximize',
              '-', 'Table',
              '-', 'BulletedList', 'NumberedList',
              '-', 'PasteText','PasteFromWord',
            ]
        ],
        'height': 120,
        'width': 640,
        'disableNativeSpellChecker': False,
        'removePlugins': 'scayt,menubutton,contextmenu,liststyle,tabletools,tableresize,elementspath',
        'resize_enabled': False,
        'extraPlugins': 'equation',
    },
}

# LOGGING
# Ignore this stupid error, why would anyone EVER want to know
# when a user cancels a request?
from django.http import UnreadablePostError

def skip_unreadable_post(record):
    if record.exc_info:
        exc_type, exc_value = record.exc_info[:2]
        if isinstance(exc_value, UnreadablePostError):
            return False
    return True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'filters': {
        'supress_unreadable_post': {
            '()': 'common.logging.SuppressUnreadablePost',
         }
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING',
            'filters': ['supress_unreadable_post'],
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['supress_unreadable_post'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}


#Engrade
# http://ww7.engrade.com/api/key.php
ENGRADE_APIKEY = ''
ENGRADE_LOGIN = ''
ENGRADE_PASSWORD = ''
# School UID (admin must be connected to school)
ENGRADE_SCHOOLID = ''


#Naviance
NAVIANCE_ACCOUNT = ''
NAVIANCE_IMPORT_USERNAME = ''
NAVIANCE_USERNAME = ''
NAVIANCE_PASSWORD = ''
# username, id, or unique_id
NAVIANCE_SWORD_ID = 'username'
NAVIANCE_IMPORT_KEY = ''
NAVIANCE_EMAILS = ''

#SchoolReach
SCHOOLREACH_USERID = ''
SCHOOLREACH_PIN = ''
# The id of the list we want to integrate, don't edit this list by hand in SR
SCHOOLREACH_LIST_ID = ''

#Admissions
ADMISSIONS_DEFAULT_COUNTRY = "United States"


#Work Study
MAX_HOURS_DAY = 10
# Sync data to SugarCRM
SYNC_SUGAR = False
SUGAR_URL = ''
SUGAR_USERNAME = ''
SUGAR_PASSWORD = ''
# Strange way of storing routes that Notre Dame High School wanted, default disabled
CRND_ROUTES = False


#Attendance
# Enables option to do course based attendance
# where teacher takes attendance at each course, not just once a day
ATTENDANCE_COURSE_BASED = False


#Canvas LMS
# oauth token, you must make this in Canvas.
# https://canvas.instructure.com/doc/api/file.oauth.html
CANVAS_TOKEN = ''
CANVAS_ACCOUNT_ID = ''
CANVAS_BASE_URL = ''


# django-report-builder
REPORT_BUILDER_GLOBAL_EXPORT = True
REPORT_BUILDER_ASYNC_REPORT = True


# Default apps, settings_local.py will override them.
INSTALLED_APPS = (
    'ecwsp.work_study',
    'ecwsp.engrade_sync',
    'ecwsp.benchmarks',
    'ecwsp.benchmark_grade',
    'ecwsp.naviance_sso',
    'rosetta',
    # These can be enabled if desired but the default is off
    #'ecwsp.integrations.schoolreach',
    'ecwsp.integrations.canvas_sync',
)

COMPRESS_PRECOMPILERS = (
   ('text/coffeescript', 'coffee --compile --stdio'),
   ('text/x-scss', 'django_libsass.SassCompiler'),
)

REDIS_ADDR = os.environ.get('REDIS_1_PORT_6379_TCP_ADDR', 'localhost')
REDIS_PORT = os.environ.get('REDIS_1_PORT_6379_TCP_PORT', '6379')
REDIS_URL = os.environ.get('REDISCLOUD_URL') or 'redis://{}:{}/0'.format(REDIS_ADDR, REDIS_PORT)

from redisify import redisify
if REDIS_URL:
    CACHES = redisify(default=REDIS_URL)
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        }
    }

BROKER_URL = REDIS_URL
BROKER_TRANSPORT_OPTIONS = {
    'fanout_prefix': True,
    'fanout_patterns': True,
}

CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
from celery.schedules import crontab
CELERYBEAT_SCHEDULE = {
    'cache-grades-nightly': {
        'task': 'ecwsp.sis.tasks.build_grade_cache',
        'schedule': crontab(hour=23, minute=1),
    },
    'sent-admissions-email': {
        'task': 'ecwsp.admissions.tasks.email_admissions_new_inquiries',
        'schedule': crontab(hour=23, minute=16),
    },
    'naviance-create-students': {
        'task': 'ecwsp.naviance_sso.tasks.create_new_naviance_students',
        'schedule': crontab(hour=23, minute=31),
    },
    'volunteer-emails': {
        'task': 'ecwsp.volunteer_track.tasks.handle',
        'schedule': crontab(hour=23, minute=46),
    },
    'email_cra_nightly': {
        'task': 'email_cra_nightly',
        'schedule': crontab(hour=0, minute=1),
    },
    'update_contacts_from_sugarcrm': {
        'task': 'ecwsp.work_study.update_contacts_from_sugarcrm',
        'schedule': timedelta(minutes=30),
    },
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('GOOGLE_OAUTH2_SECRET')

# this will load additional settings from the file settings_local.py
try:
    from .settings_server import *
except ImportError:
    print("Warning: Could not import settings_server.py")
try:
    from .settings_local import *
except ImportError:
    print("Warning: Could not import settings_local.py")

try:  # prefix cache based on school name to avoid collisions.
    if SCHOOL_NAME and CACHES:
        CACHES['default']['KEY_PREFIX'] = SCHOOL_NAME
except NameError:
    pass # Not using cache

STATICFILES_FINDERS += ('dajaxice.finders.DajaxiceFinder',)
DAJAXICE_XMLHTTPREQUEST_JS_IMPORT = False # Breaks some jquery ajax stuff!

# These are required add ons that we always want to have
if MULTI_TENANT:
    SHARED_APPS = (
        'tenant_schemas',
    )
else:
    SHARED_APPS = ()

SHARED_APPS = SHARED_APPS + (
    'constance',
    'constance.backends.database',
    'ecwsp.customers',
    'ecwsp.administration',
    'south',
    'django.contrib.contenttypes',
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'django.contrib.sessions',
)
TENANT_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.admin',
    'constance.backends.database',
    'autocomplete_light',
    'social.apps.django_app.default',
    'ldap_groups',
    'ecwsp.sis',
    'ecwsp.administration',
    'ecwsp.schedule',
    'ecwsp.admissions',
    'ecwsp.alumni',
    'ecwsp.discipline',
    'ecwsp.attendance',
    'ecwsp.grades',
    'ecwsp.counseling',
    'ecwsp.standard_test',
    'south',
    'reversion',
    'djcelery',
    'localflavor',
    'dajax',
    'dajaxice',
    'ecwsp.volunteer_track',
    'daterange_filter',
    'django_filters',
    'pagination',
    'massadmin',
    'admin_export',
    'custom_field',
    'ckeditor',
    'report_builder',
    'responsive_dashboard',
    'simple_import',
    'djangobower',
    'scaffold_report',
    'django_su',
    'floppy_gumby_forms',
    'floppyforms',
    'widget_tweaks',
    'django_cached_field',
    'rest_framework',
    'api',
    'compressor',
    'constance',
    'constance.backends.database',
) + INSTALLED_APPS

INSTALLED_APPS = SHARED_APPS + TENANT_APPS
TENANT_MODEL = "customers.Client"

CONSTANCE_CONFIG = {
    'ALLOW_GOOGLE_AUTH': (False, 'Allow users to log in with Google Apps. This requires setting the email field in student and staff.'),
    'GOOGLE_ANALYTICS': ('', 'Google Analytics code UA-XXXXXX'),
    'GOOGLE_APPS_DOMAIN': ('', 'Used with ALLOW_GOOGLE_AUTH. Google Apps domain to authenticate against. Probably the part after @ on your email address. Example: myschool.com'),
    'LDAP_URL': ('', 'Ex: ldap://admin.example.com:389'),
    'LDAP_NT4_DOMAIN': ('', 'Ex: ADMIN'),
    'LDAP_BIND_USER': ('', 'Ex: ldap_user'),
    'LDAP_BIND_PASSWORD': ('', 'Bind user\'s password'),
    'LDAP_SEARCH_DN': ('', 'DC=admin,DC=example,DC=com'),
    'MIN_PASS_GRADE': ('60', 'Minimum grade required to be considered "passing"'),
    'SCHOOL_NAME': ('Unnamed School', 'School name'),
    'SCHOOL_COLOR': ('', 'hex color code. Ex: $1122FF'),
    'SET_ALL_TO_PRESENT': (False, 'If set to True, the default course attendance setting will be "present"')
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

import django
if django.get_version()[:3] != '1.7':
    INSTALLED_APPS += ('south',)
    if MULTI_TENANT:  # Would happen automatically otherwise
        SOUTH_DATABASE_ADAPTERS = {
            'default': 'south.db.postgresql_psycopg2',
        }


ON_HEROKU = False
if 'ON_HEROKU' in os.environ:
    ON_HEROKU = True

if DEBUG and not ON_HEROKU:
    INSTALLED_APPS += ('django_extensions',)

if LDAP:
    AUTHENTICATION_BACKENDS += ('ldap_groups.accounts.backends.ActiveDirectoryGroupMembershipSSLBackend',)

TEMPLATE_CONTEXT_PROCESSORS += (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)
AUTHENTICATION_BACKENDS += ('social.backends.google.GoogleOAuth2',)
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'ecwsp.sis.auth.associate_by_email',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)
SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
)

if ON_HEROKU:
    # Use S3
    INSTALLED_APPS += ('storages', 'collectfast')
    AWS_PRELOAD_METADATA = True
    AWS_QUERYSTRING_AUTH = False
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    COMPRESS_STORAGE = STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    for environment_variable in (
        'AWS_ACCESS_KEY_ID',
        'AWS_SECRET_ACCESS_KEY',
        'AWS_STORAGE_BUCKET_NAME',
    ):
        # Cower, all ye Stack Overflow pedants!
        globals()[environment_variable] = os.environ[environment_variable]
    COMPRESS_URL = STATIC_URL = 'https://{}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)
    # Use Heroku's DB
    import dj_database_url
    # Use 'local_maroon' as a fallback; useful for testing Heroku config locally
    DATABASES['default'] = dj_database_url.config()

if MULTI_TENANT:
    DATABASES['default']['ENGINE'] = 'tenant_schemas.postgresql_backend'
    MIDDLEWARE_CLASSES = ('tenant_schemas.middleware.TenantMiddleware',) + MIDDLEWARE_CLASSES

# Keep this *LAST* to avoid overwriting production DBs with test data
if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test',
        'ATOMIC_REQUESTS': True,
    }
    CELERY_ALWAYS_EAGER = True

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}
