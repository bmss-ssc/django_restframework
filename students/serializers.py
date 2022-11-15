from rest_framework import serializers

from stuapi.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        # fields = ['id', 'name', 'age']
