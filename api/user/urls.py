from django.urls import path, include
from rest_framework import routers
from user import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
]