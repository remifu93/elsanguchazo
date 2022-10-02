from django.apps import AppConfig


class OptionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'option'
    verbose_name = 'Comidas'
    
    def ready(self):
        from . import signals
        