# django-amp-readerid
Manage the user association with the AMP reader ids

# Sorry, this app is not implemented yet. It will be implemented soon (estimated for this month, May 2023), the idea is:

Associate AMP readers ids with timestamp of "last used" when there is a successful login from amp, for that we can use the user_logged_in signal: https://stackoverflow.com/a/6109366/2292933 (but how we can operate if the user is alreade logged in? a middleware instead of a signal can be another solution, also check the AMP docs for the login and logout endpoints, may help to solve this point)

That app will also have a management command that can be used via cron to remove old reader ids that haven't been used for X amount of time.

In the amp_user_auth view of your site, you could also update the timestamp, write here that this is responsibility of the developer.

Also implement "utils" to quickly get the user associated with an amp request, for example for the amp_user_auth view or the pingback view.
