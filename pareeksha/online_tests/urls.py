from django.conf.urls import include, url
from rest_framework import routers

from .views import OnlineTestViewSet

router = routers.DefaultRouter()
router.register('online_tests', OnlineTestViewSet, base_name='online_tests')

urlpatterns = [
    url("^", include(router.urls)),
]