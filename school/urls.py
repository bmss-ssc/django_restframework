from rest_framework.routers import SimpleRouter, DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()
router.register(prefix='students', viewset=views.StudentViewSet, basename='students')

urlpatterns = [

              ] + router.urls
