"""
TODO:
We should implement a decorator here for the amp-login view, things to take care in the decorator:
 - the parameter name of the "readerID" included in the GET request
 - the login view can already set some variables to redirect to a "next" or "return" URL, we must not change anything
   of this behaviour, unless the reader ID is received, this indicates that this is a login from AMP and the request
   also should came with a "return" parameter to redirect (an "url" param may also be received, for the page where the
   login was clicked, this may be used instead of the "return" in dev time, because dev page will not be cached in
   google)
"""
