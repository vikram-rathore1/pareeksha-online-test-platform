from django.conf.urls import include, url
from .views import LoginAPI

urlpatterns = [
    url("^login/", LoginAPI.as_view()),
]