from django.conf import settings

from django.contrib.auth.signals import user_logged_in


def amp_readerid_assoc(sender, user, request, **kwargs):
    reader_id = request.session.pop("amp_reader_id", None)
    if settings.DEBUG:
        print("rid in session: %s" % reader_id)
    if reader_id:
        # TODO: set/refresh assoc
        pass

user_logged_in.connect(amp_readerid_assoc)
