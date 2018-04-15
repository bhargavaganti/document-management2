from django.urls import path, include
from rest_framework import routers
from document import views

router = routers.DefaultRouter()
router.register('documents', views.DocumentViewset)
router.register('customers', views.CustomerViewset)
router.register('packages', views.PackageViewset)

# Wire up our API using automatic URL routing.

urlpatterns = [
    path('', include(router.urls)),
]