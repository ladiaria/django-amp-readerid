from django.urls import path

from .views import redirect


app_name = "amp-readerid"
urlpatterns = [path("redirect/", redirect, name="redirect")]
