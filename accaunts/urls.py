from django.urls import path

from rest_framework.routers import SimpleRouter
from .views import  UserViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken import views
from django.urls import path, include, re_path
from django.contrib.auth.models import User


router = SimpleRouter()
router.register('', UserViewSet, basename='user')

urlpatterns = router.urls

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration', include('dj_rest_auth.registration.urls')),
    path('allauth', include('allauth.urls')),
    path('api-token-auth/', views.obtain_auth_token)
]