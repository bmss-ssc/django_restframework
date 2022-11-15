from rest_framework.viewsets import ModelViewSet

from school.models import Student
from school.serializers import StudentModelSerializer2


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer2
