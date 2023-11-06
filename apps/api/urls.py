from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ClientViewSet

router = DefaultRouter()
router.register('client', ClientViewSet, basename='client')

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]

urlpatterns += router.urls