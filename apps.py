from django.apps import AppConfig
from django.conf import settings

class UtentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'utents'
    settings.AUTH_USER_MODEL = 'utents.Utent'
    settings.LOGIN_REDIRECT_URL = '/'
    settings.LOGOUT_REDIRECT_URL = '/'