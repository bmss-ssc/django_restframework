from rest_framework.viewsets import ModelViewSet
from stuapi.models import Student
from .serializers import StudentSerializer


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
