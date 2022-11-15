from django.urls import path
from . import views

urlpatterns = [
    path('example/', views.ExampleView.as_view()),
    path('home/', views.HomeAPIView.as_view()),
    path('home/info/', views.HomeInfoAPIView.as_view()),
    path('students/<int:pk>/', views.Home2InfoAPIView.as_view()),
    path('demo1/', views.Demo1APIView.as_view()),
    path('demo2/', views.Demo2APIView.as_view()),
    path('demo3/', views.Demo3APIView.as_view()),
    path('demo4/', views.Demo4APIView.as_view()),
    path('demo5/', views.Demo5APIView.as_view()),
]
