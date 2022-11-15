from django.urls import path, re_path
from stuapi import views

urlpatterns = [
    path("students/", views.StudentView.as_view()),
    re_path("^students/(?P<pk>\d+)/$", views.StudentInfo.as_view()),
]
