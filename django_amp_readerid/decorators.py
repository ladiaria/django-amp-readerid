from django.conf import settings


def readerid_assoc(login_view):
    """
    TODO: decorator for the amp-login view, things to take care in the decorator:
    - if form is not valid in post phase
    - the parameter name of the "readerID" included in the GET request (should be an app setting)
    - the login view can already set some variables to redirect to a "next" or "return" URL, we must not change anything
      of this behaviour, unless the reader ID is received, this indicates that this is a login from AMP and the request
      also should came with a "return" parameter to redirect (in dev time the param value may need rerwited, because dev
      page will not be cached in google)
    """

    def assoc(request, *args, **kwargs):
        if settings.DEBUG:
            print(request.GET)##
        return login_view(request, *args, **kwargs)

    return assoc
