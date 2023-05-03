# django-amp-readerid
Manage the user association with the AMP reader ids

# Sorry, this app is not finished yet. It will be finished and first-released soon (estimated for this month, May 2023), the idea is:

Associate AMP readers ids (upto some limit, for ex 10, round-robin oldest) with timestamp of "last used" when there is a successful login from amp, for that we use the user_logged_in signal: https://stackoverflow.com/a/6109366/2292933 (see signals.py) and also a decorator to be used in the amp-login view (see decorators.py).

**IMPORTANT:** The implementation of the amp-login view and how it redirects after a successfull login is site dev's responsibility. TODO: provide a minimal example and also warn when using google-social-auth.

TODO: a management command that can be used via cron to remove old reader ids that haven't been used for X amount of time.

In the amp_user_auth view of your site, you could also update the timestamp, TODO: write here that this is responsibility of the developer too.

## Utilities:

 - get the user associated with an amp request, for example for the amp_user_auth view or the pingback view.
 - A function that returns True when the request has all the get params used for the login requests originated from an AMP page.
 - A view to redirect to an url given by param (useful when using google-social-auth).
