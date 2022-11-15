from django.urls import path, re_path, include
from demo import views
from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter()
router.register(prefix='viewsets', viewset=views.StudentViewSet)

urlpatterns = [
    path('students/', views.StudentAPIView.as_view()),
    path('students/<int:pk>/', views.StudentInfoAPIView.as_view()),
    # Generic APIView
    path('students2/', views.StudentGenericAPIView.as_view()),
    path('students2/<int:pk>/', views.StudentInfoGenericAPIView.as_view()),
    # re_path('^students2/(?P<pk>\d+)/$', views.StudentGenericAPIView.as_view()),
    # Generic mixins APIView
    path('students3/', views.StudentMixinView.as_view()),
    path('students3/<int:pk>/', views.StudentInfoMixinView.as_view()),

    # path('students4/', views.StudentViewSet.as_view({
    #     'get': 'login'
    # })),

    # DRF Viewsets
    # path('viewsets/', views.StudentViewSet.as_view({
    #     'get': 'list', 'post': 'create'
    # })),
    # path('viewsets/<int:pk>/', views.StudentViewSet.as_view({
    #     'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    # })),
    path("", include(router.urls))

]
