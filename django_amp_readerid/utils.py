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
    Relates a reader_id with a user:
    - if already related with trhe same user: only save object to update the last_used timestamp.
    - if already related with another user, because more than one user have used the device loggede-in (common in dev):
        change the user and save.
    - On any case, check for the max relation limit, and replace/remove the oldest one to keep limits consistently.
    """

    try:

        related_obj = UserReaderId.objects.get(reader_id=reader_id)

    except UserReaderId.DoesNotExist:

        related_set = user.userreaderid_set
        if related_set.count() < app_settings.MAX_READER_IDS_PER_USER:
            # safe to create
            UserReaderId.objects.create(reader_id=reader_id, user=user)
        else:
            # update earliest user's relation
            related_obj = related_set.earliest()
            related_obj.reader_id = reader_id
            related_obj.save()

    else:

        if related_obj.user == user:
            related_obj.save()
        else:

            related_set = user.userreaderid_set
            if related_set.count() >= app_settings.MAX_READER_IDS_PER_USER:
                # remove user earlies't one
                related_set.earliest().delete()

            # now is safe to update the user
            related_obj.user = user
            related_obj.save()


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
            pass
        else:
            r.save()
            return r.user
    return request.user
