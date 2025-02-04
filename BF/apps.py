# BF/apps.py
from django.apps import AppConfig

class BfConfig(AppConfig):
    name = 'BF'

    def ready(self):
        import BF.signals


