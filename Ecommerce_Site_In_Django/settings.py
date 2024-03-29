from pathlib import Path

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-^=&+sdmoes1^%@9x64b^gq#ntg+oj5w=93egt!s1b!h+@zvkmm"

DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django_admin_kubi',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'accounts.apps.AccountsConfig',
    'shop.apps.ShopConfig',
    'sorl.thumbnail',
    'crispy_forms',
    'crispy_bootstrap5',
    'phonenumber_field',
    'rosetta',
    'django_cleanup.apps.CleanupConfig',
]

PHONENUMBER_DEFAULT_REGION = "KE"

AUTH_USER_MODEL = 'accounts.Account'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

DJANGO_ADMIN_KUBI = {
    'ADMIN_HISTORY': True,  # enables the history action panel
    'ADMIN_SEARCH': True,  # enables a full modal search
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Ecommerce_Site_In_Django.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "shop.context_processor.basket",
            ],
        },
    },
]

WSGI_APPLICATION = "Ecommerce_Site_In_Django.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.environ.get('HOST_EMAIL')
# EMAIL_HOST_PASSWORD = os.environ.get('HOST_EMAIL_PASSWORD')

LOGIN_URL = reverse_lazy('accounts:user-login')
LOGIN_REDIRECT_URL = reverse_lazy('shop:index')

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# redis cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

LANGUAGE_CODE = "en"

TIME_ZONE = "Africa/Nairobi"

USE_I18N = True
USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
    ('sw', _('Swahili')),
)
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
