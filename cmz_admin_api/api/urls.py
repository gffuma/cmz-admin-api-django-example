from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers
from .views import NewsViewSet
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', obtain_jwt_token)
]
