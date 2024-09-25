from pathlib import Path
from utils.constants import SettingsConstants
from os.path import join

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# -------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Root URL Config: Django Package / urls.
# -------------------------------------------------------------------
ROOT_URLCONF = "drf.urls"

# SECURITY WARNING: keep the secret key used in production secret!
# -------------------------------------------------------------------
SECRET_KEY = SettingsConstants.SECRET_KEY.value

# INSTALLED APPS: Required Apps + Installed Django Apps + Third Party Packages!
# -------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
]

# INSTALLED APPS: Required Apps + Installed Django Apps + Third Party Packages!
# -------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# Templates: Template Director + Context Processors!
# -------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [join(BASE_DIR, SettingsConstants.TEMPLATES.value)],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "utils.context_processors.theme_form",
                "utils.context_processors.newsletter_form",
            ],
        },
    },
]

# WSGI Apllication Constant!
# -------------------------------------------------------------------
WSGI_APPLICATION = SettingsConstants.WSGI_APPLICATION.value

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# -------------------------------------------------------------------
DATABASES = {"default": SettingsConstants.DATABASE_URL.value}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
# -------------------------------------------------------------------
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

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
# -------------------------------------------------------------------
LANGUAGE_CODE = SettingsConstants.LANGUAGE_CODE.value

TIME_ZONE = SettingsConstants.TIME_ZONE.value

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = SettingsConstants.STATIC_URL.value
STATICFILES_DIRS = [join(BASE_DIR, SettingsConstants.STATISFILES_DIRS.value)]
STATIC_ROOT = SettingsConstants.STATIC_ROOT.value


# Models Media Files
MEDIA_URL = SettingsConstants.MEDIA_URL.value
MEDIA_ROOT = SettingsConstants.MEDIA_ROOT.value

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = SettingsConstants.DEFAULT_AUTO_FIELD.value

# Debug Toolbar Configuration
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
INTERNAL_IPS = SettingsConstants.INTERNAL_IPS.value
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.alerts.AlertsPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]
DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}
DEBUG_TOOLBAR_PATCH_SETTINGS = True
