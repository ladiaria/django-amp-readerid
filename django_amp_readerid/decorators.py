from django.conf import settings


def readerid_assoc(login_view):
    """
    decorator for the amp-login view, TODO: explain how it works.
    """

    def assoc(request, *args, **kwargs):
        if request.method == 'GET':
            return_url = request.GET.get("return")
            reader_id = request.GET.get("rid")  # TODO: use setting
            if return_url and reader_id:  # TODO: other custom params (by settings) should be present
                if request.user.is_authenticated:
                    # TODO: set/refresh assoc only
                    pass
                else:
                    request.session["amp_reader_id"] = reader_id
        return login_view(request, *args, **kwargs)

    return assoc
