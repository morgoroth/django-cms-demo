# Django settings for demo project.
import sys
import os
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0, PROJECT_DIR)

gettext = lambda s: s

LANG="en_US.UTF-8"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'demo.db',
    'HOST': '',
    'PORT': '',
    'USER': '',
    'PASSWORD': ''
  }
}

#To set up Heroku caching use the add on MemCachier and input your credentials here
import herokuify
CACHES = herokuify.get_cache_config()   # Memcache config for Memcache/MemCachier

COMPRESS_STORAGE = "herokuify.storage.CachedS3StaticStorage"
COMPRESS_OFFLINE = True
ROBOTS_CACHE_TIMEOUT = 60*60*24

#To set up Amazon S3 media hosting just input your bucket information below

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_QUERYSTRING_AUTH = True
AWS_STORAGE_BUCKET_NAME = 'demo-cms-heroku'

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'https://s3.amazonaws.com/demo-cms-heroku/'

TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
import os; os.environ['LANG'] = 'en_US.UTF-8'
LANGUAGE_CODE = 'en-us'


SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_DIR, "apps/blog/media")
MEDIA_URL = '/media/'

STATIC_ROOT = S3_URL
STATIC_URL = S3_URL

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, "apps/blog/site-static"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'kr&amp;m^8_$@=%_%v*o@!$t2qye_bz3ohkrh_ug3^rhq)w99apuaj'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware', #CMS
    'cms.middleware.page.CurrentPageMiddleware', #CMS
    'cms.middleware.user.CurrentUserMiddleware', #CMS
    'cms.middleware.toolbar.ToolbarMiddleware', #CMS
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media', #CMS
    'sekizai.context_processors.sekizai', #CMS
)

ROOT_URLCONF = 'demo.urls'

WSGI_APPLICATION = 'demo.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, "apps/blog/templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # CMS related apps
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'reversion',
    'cms.plugins.text',
#    'demo.apps.blog.polls', //TODO delete
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_file',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'cms.plugins.link',
    'demo.apps.blog.plugins.bootstrap_button',
    'herokuify',
    'storages',
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# django CMS settings
LANGUAGES = [
    ('en', gettext('English')),
]

CMS_LANGUAGES = LANGUAGES
CMS_HIDE_UNTRANSLATED = True
CMS_LANGUAGE_CONF = {
        'es': ['en',],
    }


CMS_TEMPLATES = (
    ('home.html', gettext("Homepage")),
    ('subpage.html', gettext("Secondary Page")),
)

CMS_PLACEHOLDER_CONF = {
    'home-hero': {
        'name': gettext('Hero'),
        'plugins': ['TextPlugin', 'BootstrapButtonPlugin',],
    },
    'home-col-1': {
        'name': gettext('Column 1'),
        'plugins': ['TextPlugin', 'BootstrapButtonPlugin',],
    },
    'home-col-2': {
        'name': gettext('Column 2'),
        'plugins': ['TextPlugin', 'BootstrapButtonPlugin',],
    },
    'home-col-3': {
        'name': gettext('Column 3'),
        'plugins': ['TextPlugin', 'PollPlugin', ],
        'limits': {
            'global': 2,
            'TextPlugin': 1,
            'PollPlugin': 1,
        },
    },
    'subpage_content': {
        'name': gettext('Content'),
    },
}

CMS_URL_OVERWRITE = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_REDIRECTS = True
CMS_SOFTROOT = True
CMS_PERMISSION = True
CMS_SHOW_START_DATE = True
CMS_SHOW_END_DATE = True 
CMS_SEO_FIELDS = True 

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
