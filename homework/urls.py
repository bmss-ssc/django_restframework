from rest_framework.routers import DefaultRouter
from django.urls import path
from homework import views

router = DefaultRouter()
router.register(prefix='courses4', viewset=views.CourseViewSet)

urlpatterns = [
                  # 1.基于APIView编写5个API接口
                  path('courses1/', views.CourseAPIView.as_view()),
                  path('courses1/<int:pk>/', views.CourseInfoAPIView.as_view()),

                  # 2.基于GenericAPIView编写5个API接口
                  path('courses2/', views.CourseGenericAPIView.as_view()),
                  path('courses2/<int:pk>/', views.CourseInfoGenericAPIView.as_view()),
                  # 3.基于GenericAPIView+Mixins编写5个API接口
                  path('courses3/', views.CourseMixinsGenericAPIView.as_view()),
                  path('courses3/<int:pk>/', views.CourseInfoMixinsGenericAPIView.as_view()),
              ] + router.urls
