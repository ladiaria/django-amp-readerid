from django.apps import AppConfig


class DjangoAmpReaderidConfig(AppConfig):
    name = 'django_amp_readerid'

    # default configuration values matching https://amp.dev/documentation/components/amp-access#configuration
    READER_ID_PARAM_NAME = "rid"
    EXTRA_PARAMS = ["url"]
    # allow upto this number of different reader ids per user
    MAX_READER_IDS_PER_USER = 10

    def ready(self):
        import django_amp_readerid.signals  # noqa
