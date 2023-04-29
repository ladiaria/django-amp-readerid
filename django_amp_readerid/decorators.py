"""
TODO:
We should implement a decorator here for the amp-login view, update readme (no signal or middleware, decorator!)
Also for readme: implement the amp-login view is site dev's responsibility
Things to take care in the decorator:
 - the parameter name of the "readerID" included in the GET request
 - the login view can already set some variables to redirect to a "next" or "return" URL, we must not change anything
   of this behaviour, unless the reader ID is received, this indicates that this is a login from AMP and the request
   also should came with a "return" parameter to redirect
"""
