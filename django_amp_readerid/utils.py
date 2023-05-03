from .apps import DjangoAmpReaderidConfig as app_settings
from .models import UserReaderId


def amp_login_param(request, param_name):
    """
    Returns the param value for the param @param_name only if the request GET params has all the params that indicates
    that is a request originated from AMP, based on the amp_access configuration and this app settings.
    Otherwise returns None.
    """
    if all(k in request.GET for k in ["return", app_settings.READER_ID_PARAM_NAME] + app_settings.EXTRA_PARAMS):
        return request.GET[param_name]


def amp_login_readerid(request):
    """ amp_login_param wrapper for the reader_id param """
    return amp_login_param(request, app_settings.READER_ID_PARAM_NAME)


def relate(reader_id, user):
    """
    relates a reader_id with a user
    if already related, save object to update the last_used timestamp
    if max relations reached, replaces the oldest one
    """
    if user.userreaderid_set.count() < app_settings.MAX_READER_IDS_PER_USER:
        r, created = UserReaderId.objects.get_or_create(reader_id=reader_id, user=user)
        if not created:
            r.save()
    else:
        r = user.userreaderid_set.earliest()
        r.reader_id = reader_id
        r.save()


def amp_readerid(request):
    """ returns the reader id param value of the request """
    return request.GET.get(app_settings.READER_ID_PARAM_NAME)


def get_related_user(request):
    """
    Returns the related user with the request's reader_id (if any), and updates the "last_used" timestamp.
    If no user related, returns the request.user attribute.
    """
    reader_id = amp_readerid(request)
    if reader_id:
        try:
            r = UserReaderId.objects.get(reader_id=reader_id)
        except UserReaderId.DoesNotExist:
            if request.user.is_authenticated:
                relate(reader_id, request.user)
        else:
            r.save()
            return r.user
    return request.user
