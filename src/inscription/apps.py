from django.apps import AppConfig


class InscriptionConfig(AppConfig):
    name = 'inscription'

    def ready(self):
        from . import signals
