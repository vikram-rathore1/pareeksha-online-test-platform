from django.conf.urls import include, url
from .views import LoginAPI, RegistrationAPI

urlpatterns = [
    url("^login/", LoginAPI.as_view()),
    url("^register/", RegistrationAPI.as_view()),
]