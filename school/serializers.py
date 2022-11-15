from rest_framework import serializers

from school.models import Student, Achievement, Course


class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name']


class AchievementModelSerializer(serializers.ModelSerializer):
    # course = CourseModelSerializer()
    course_name = serializers.CharField(source='course.name')
    teacher_name = serializers.CharField(source='course.teacher.name')

    class Meta:
        model = Achievement
        fields = ['id', 'course_name', 'teacher_name', 'score', 'create_dtime']


class AchievementModelSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'
        depth = 2


class StudentModelSerializer2(serializers.ModelSerializer):
    s_achievement = AchievementModelSerializer(many=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'sex', 's_achievement']
