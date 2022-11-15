from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()
route.register('students2', views.StudentModelViewSet, basename='students2')

urlpatterns = [] + route.urls
