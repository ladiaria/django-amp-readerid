from django.conf import settings
from django.contrib.auth.signals import user_logged_in

from .utils import relate


def amp_readerid_assoc(sender, user, request, **kwargs):
    reader_id = request.session.pop("amp_reader_id", None)
    if settings.DEBUG:
        print("rid in session: %s" % reader_id)
    if reader_id:
        relate(reader_id, user)


user_logged_in.connect(amp_readerid_assoc)
