import os
from pathlib import Path
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Loader:
    """
    Main class for managing environment variables.
    Adjust URL section and below according to selected resource.
    """

    # Django secret key.
    secret_key: str = os.getenv('SECRET_KEY')

    # Debug settings.
    debug: bool = bool(os.getenv('DEBUG'))

    # URLs.
    main_url: str = os.getenv('MAIN_URL')
    sword_url: str = os.getenv('SWORD_URL')
    claymore_url: str = os.getenv('CLAYMORE_URL')
    polearm_url: str = os.getenv('POLEARM_URL')
    bow_url: str = os.getenv('BOW_URL')
    catalyst_url: str = os.getenv('CATALYST_URL')

    # Main data.
    main_data = os.getenv('MAIN_DATA')

    # Main class.
    main_class: str = os.getenv('MAIN_CLASS')
    stat_class: str = os.getenv('STAT_CLASS')

    # Main elements.
    main_elem: str = os.getenv('MAIN_ELEM')
    second_elem: str = os.getenv('SECOND_ELEM')

    # Character page elements.
    character_urls: str = os.getenv('CHAR_LIST_URL')
    character_skill_class: str = os.getenv('SKILL_CLASS')
    character_dmg_class: str = os.getenv('DMG_CLASS')
    character_elem_number: int = int(os.getenv('CHARACTER_ELEMENTS_NUMBER'))

    # Weapon page elements.
    weapon_elem_number: int = int(os.getenv('WEAPON_ELEMENTS_NUMBER'))


env_loader = Loader()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env_loader.secret_key

DEBUG = env_loader.debug

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
    'data',
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

ROOT_URLCONF = 'genshin_calculator.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'genshin_calculator.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
