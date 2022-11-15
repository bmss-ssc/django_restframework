from django.urls import path
from req import views

urlpatterns = [
    path('students/', views.StudentAPIView.as_view()),
]
