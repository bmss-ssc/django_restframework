from django.urls import path
from sers import views

urlpatterns = [
    path('students/', views.StudentView.as_view()),
]
