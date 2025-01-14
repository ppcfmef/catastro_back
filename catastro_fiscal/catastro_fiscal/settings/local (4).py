import dj_database_url
import redis
from .base import *  # noqa: F403

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env(  # noqa: F405
    "DJANGO_SECRET_KEY",
    default='INSERT_KEY_HERE'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=True)  # noqa: F405

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=['*'])  # noqa: F405

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASE_OPTION_DRIVER = env("DATABASE_OPTION_DRIVER", default='ODBC Driver 17 for SQL Server')   # noqa: F405

DB_DEFAULT_CONFIG = dj_database_url.config(
    default=env(  # noqa: F405
        "DATABASE_URL",
        default=f"sqlite:///{ BASE_DIR / 'db.sqlite3' }"  # noqa: F405
    )
)

if DB_DEFAULT_CONFIG.get("ENGINE") == 'mssql':  #  'sql_server.pyodbc':
    DB_DEFAULT_CONFIG.update({
        'OPTIONS': {'driver': DATABASE_OPTION_DRIVER}
    })

DATABASES = {
    'default': DB_DEFAULT_CONFIG
}

# API Rest
CORS_ALLOW_CREDENTIALS = env.bool("CORS_ALLOW_CREDENTIALS", True)  # noqa: F405
CORS_ORIGIN_ALLOW_ALL = env.bool("CORS_ORIGIN_ALLOW_ALL", True)  # noqa: F405
if not CORS_ORIGIN_ALLOW_ALL:
    CORS_ORIGIN_WHITELIST = env.list("CORS_ORIGIN_WHITELIST")  # noqa: F405

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

DEPLOY_URL_PATH = env("DEPLOY_URL_PATH", default="plataformaCF/catastroback/")   # noqa: F405

STATIC_URL = '/plataformaCF/catastroback/static/'
STATICFILES_DIR = [
    BASE_DIR / 'static',  # noqa: F405
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # noqa: F405

MEDIA_URL = '/plataformaCF/catastroback/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # noqa: F405

URL_API_PERSONS = env("URL_API_PERSONS", default='')   # noqa: F405
KEY_API_PERSONS = env("KEY_API_PERSONS", default='')   # noqa: F405
URL_API_BUSINESS = env("URL_API_BUSINESS", default='')  # noqa: F405
KEY_API_BUSINESS = env("KEY_API_BUSINESS", default='')  # noqa: F405

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': env("CACHE_LOCATION_DIR", default=str(BASE_DIR / 'django_cache')),  # noqa: F405
        'MAX_ENTRIES': 10000,
    }
}

DRAMATIQ_REDIS_URL = env("REDIS_URL", default="redis://:lUdkuymE@10.5.116.28:6379/0")
DRAMATIQ_BROKER = {
    "BROKER": "dramatiq.brokers.redis.RedisBroker",
    "OPTIONS": {
        "connection_pool": redis.ConnectionPool.from_url(DRAMATIQ_REDIS_URL),
    },
    "MIDDLEWARE": [
        "dramatiq.middleware.AgeLimit",
        "dramatiq.middleware.TimeLimit",
        "dramatiq.middleware.Retries",
        "django_dramatiq.middleware.AdminMiddleware",
        "django_dramatiq.middleware.DbConnectionsMiddleware",
    ]
}

API_KEY_QUERY_PARAM = 'mobileApiKey'
URL_API_NSRTM = env("URL_API_NSRTM", default='')
URL_API_SATT = env("URL_API_SATT", default='')
HOST_REFERER =  'http://localhost:4200/'
#HOST_REFERER = 'https://appstest.mineco.gob.pe' # test
