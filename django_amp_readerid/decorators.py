from .utils import amp_login_readerid, relate


def readerid_assoc(login_view):
    """
    decorator for the amp-login view, TODO: explain how it works.
    """

    def assoc(request, *args, **kwargs):
        if request.method == 'GET':
            reader_id = amp_login_readerid(request)
            if reader_id:
                if request.user.is_authenticated:
                    relate(reader_id, request.user)
                else:
                    request.session["amp_reader_id"] = reader_id
        return login_view(request, *args, **kwargs)

    return assoc
