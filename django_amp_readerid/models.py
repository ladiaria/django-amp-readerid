from django.db import models
from django.contrib.auth.models import User

from .apps import DjangoAmpReaderidConfig as app_settings


class UserReaderId(models.Model):
    reader_id = models.CharField(max_length=32, unique=True)
    last_used = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        get_latest_by = "last_used"

    def __str__(self):
        return "%s @ %s on %s" % (self.user, self.reader_id, self.last_used)
