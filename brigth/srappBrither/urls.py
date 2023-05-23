from django.urls import path,include
from rest_framework import routers
from .views import JobViewSet


routes=routers.DefaultRouter()
routes.register(r'jobs',JobViewSet)

urlpatterns = [
    path('',include(routes.urls))
]
