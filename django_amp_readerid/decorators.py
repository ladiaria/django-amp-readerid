from django.contrib.auth.signals import user_logged_in


def amp_readerid_assoc(sender, user, request, **kwargs):
    print("DEBUG: amp_readerid_assoc signal request: %s" % request)##


# TODO: we should use a decorator for the amp-login view, update readme (no signal or middleware, decorator!)
#       Also for readme: implement the amp-login view is site dev's responsibility
user_logged_in.connect(do_stuff)
