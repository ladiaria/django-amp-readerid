from django.apps import AppConfig


class DjangoAmpReaderidConfig(AppConfig):
    name = 'django_amp_readerid'

    def ready(self):
        import django_amp_readerid.signals
