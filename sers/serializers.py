from rest_framework import serializers

from stuapi.models import Student


class Student1Serializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    sex = serializers.BooleanField()
    age = serializers.IntegerField()
    description = serializers.CharField()


def check_classmate(data):
    if len(data) != 3:
        raise serializers.ValidationError(detail='班级编号格式不正确，必须是3个字符', code='check_classmate')
    return data


class Student2Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    sex = serializers.BooleanField(default=True)
    age = serializers.IntegerField(required=True, max_value=100, min_value=0, error_messages={
        'max_value': 'The age filed Must Be age <= 100',
        'min_value': 'The age filed Must Be age >= 0',
    })
    # validators 外部函数验证选项，值是一个列表，列表是函数名，不是字符串
    classmate = serializers.CharField(required=True, validators=[check_classmate])
    description = serializers.CharField(allow_null=True, allow_blank=True)

    def validate(self, attrs):
        # 验证来自客户端的所有数据
        if attrs['classmate'] == '307' and attrs['sex']:
            raise serializers.ValidationError(detail='307班只能进去小姐姐!', code='validate')
        return attrs

    def validate_name(self, data):
        # 验证单个字段， 方法格式 validate_<字段名>
        if data in ['python', 'django']:
            raise serializers.ValidationError(detail='学生名不能是python或者Django', code='validate')

        return data

    def create(self, validated_data):
        student = Student.objects.create(**validated_data)

        return student

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.sex = validated_data['sex']
        instance.age = validated_data['age']
        instance.classmate = validated_data['classmate']
        instance.description = validated_data['description']

        return instance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        # fields = []
        # read_only_fields = []
        # exclude = []
        extra_kwargs = {
            'age': {
                'max_value': 100,
                'min_value': 0,
                'error_messages': {
                    'max_value': '年龄最大值必须小于等于100',
                    'min_value': '年龄最小值必须大于等于0',
                }
            }
        }
