from django.http import HttpResponseRedirect


def redirect(request):
    return HttpResponseRedirect(request.GET.get("url", "/"))
