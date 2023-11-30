from django.apps import AppConfig


class InheritAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inherit_app'
