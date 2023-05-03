# django-amp-readerid
Utilities to manage the user association with the AMP reader ids.

Associates AMP readers ids with timestamp of "last used" when there is a successful login from amp, for that we use the user_logged_in signal: https://stackoverflow.com/a/6109366/2292933 (see signals.py) and also a decorator to be used in the amp-login view (see decorators.py).

**IMPORTANT:** The implementation of the amp-login view and how it redirects after a successfull login is site dev's responsibility. TODO: provide a minimal example and also warn when using google-social-auth.

TODO: a management command that can be used via cron to remove old reader ids that haven't been used for X amount of time. Or as many older entries to keep limits per user consistenlty with the configuration.

In the amp_user_auth view of your site, you could also update the timestamp, TODO: write here that this is responsibility of the developer too showing an usage example.

## Utilities:

 - get the user associated with an amp request, for example for the amp_user_auth view or the pingback view.
 - A function that returns a param value given by name when the request has all the get params used for the login requests originated from an AMP page.
 - A view to redirect to an url given by param (useful when using google-social-auth).

## Django and Python versions:

This app was only tested in Django 2.2.28 and Python from 3.10.6 to 3.10.11

Upgrade to Django 4 is expected to be checked/implemented soon (next month, June 2023).

## Installation:

TODO: write this topic

## Configuration and usage:

TODO: write this topic

## Usage examples:

TODO: Link to utopia-cms files with explanation
