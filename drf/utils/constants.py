from enum import Enum
from dotenv import dotenv_values
from dj_database_url import parse as db_url

config = dotenv_values(".env")


# Settings Constants
# -------------------------------------------------------------------
class SettingsConstants(Enum):
    SECRET_KEY = config.get("SECRET_KEY")
    TEMPLATES = "templates/"
    STATIC_URL = "static/"
    STATISFILES_DIRS = "templates/static/"
    STATIC_ROOT = "assets/"
    MEDIA_URL = "media/"
    MEDIA_ROOT = "media/"
    WSGI_APPLICATION = "drf.wsgi.application"
    DATABASE_URL = db_url(config.get("DJANGO_DATABASE_URL"))
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "Asia/Kolkata"
    INTERNAL_IPS = [
        "127.0.0.1",
    ]


# Template Paths.
# -------------------------------------------------------------------
class Templates(Enum):
    BASE = "base.html"
    ABOUT = "drf/about.html"


# DRF Urls & Urls Reverse.
# -------------------------------------------------------------------
class Urls(Enum):
    INDEX_REVERSE = "index"
    ABOUT_REVERSE = "about"


# Extra Constants.
# -------------------------------------------------------------------
EMPTY_STR = ""
UTF_8 = "utf-8"
FORM_CLASS = "input input-bordered w-full"
FORM_CLASS_FILE = "file-input file-input-bordered w-full"
TEXT_AREA = "textarea textarea-bordered textarea-lg w-full"
SELECT_CLASS = "select select-bordered w-full select-sm"
THEME_CHOICES = (
    ("light", "light"),
    ("dark", "dark"),
    ("cupcake", "cupcake"),
    ("bumblebee", "bumblebee"),
    ("emerald", "emerald"),
    ("corporate", "corporate"),
    ("synthwave", "synthwave"),
    ("retro", "retro"),
    ("cyberpunk", "cyberpunk"),
    ("valentine", "valentine"),
    ("halloween", "halloween"),
    ("garden", "garden"),
    ("forest", "forest"),
    ("aqua", "aqua"),
    ("lofi", "lofi"),
    ("pastel", "pastel"),
    ("fantasy", "fantasy"),
    ("wireframe", "wireframe"),
    ("black", "black"),
    ("luxury", "luxury"),
    ("dracula", "dracula"),
    ("cmyk", "cmyk"),
    ("autumn", "autumn"),
    ("business", "business"),
    ("acid", "acid"),
    ("lemonade", "lemonade"),
    ("night", "night"),
    ("coffee", "coffee"),
    ("winter", "winter"),
    ("dim", "dim"),
    ("nord", "nord"),
    ("sunset", "sunset"),
)
