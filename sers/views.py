from django.http import JsonResponse
from django.views import View

from sers.serializers import Student1Serializer, Student2Serializer, StudentSerializer
from stuapi.models import Student


class Student1View(View):
    def get1(self, request):
        # 获取一个序列化对象
        # 1.获取数据集
        instance = Student.objects.first()
        # 2.实例化序列化器，得到序列化对象
        serializer = Student1Serializer(instance=instance)
        # 3.调用序列化对象的data属性方法获取转换后的数据
        data = serializer.data
        # 4.响应数据
        return JsonResponse(data=data, status=200, safe=False)

    def get2(self, request):
        # 获取多个序列化对象
        # 1.获取数据集
        student_list = Student.objects.all()
        # 2.实例化序列化器，得到序列化对象
        serializer = Student1Serializer(instance=student_list, many=True)
        # 3.调用序列化对象的data属性方法获取转换后的数据
        data = serializer.data
        # 4.响应数据
        return JsonResponse(data=data, status=200, safe=False)

    def get4(self, request):
        # 1.接收客户端提交的数据
        data = {
            'name': 'ssc',
            'sex': True,
            'age': 18,
            'classmate': '301',
            'description': 'hahahahha'
        }
        # 1.1实例化序列化器，获取序列化对象
        serializer = Student2Serializer(data=data)
        # 1.2调用序列化器进行数据验证
        # serializer.is_valid() #不抛出异常
        serializer.is_valid(raise_exception=True)
        # 1.3获取验证后的结果
        print(serializer.validated_data)
        # 2.操作数据库
        # 3.返回响应
        return JsonResponse(data=serializer.data)

    def get5(self, request):
        # 验证完成，添加数据入库
        # 1.接收客户端提交的数据
        data = {
            'name': 'ssc1',
            'sex': True,
            'age': 27,
            'classmate': '301',
            'description': 'hahahahha'
        }
        # 1.1实例化序列化器，获取序列化对象
        serializer = Student2Serializer(data=data)
        # 1.2调用序列化器进行数据验证
        # serializer.is_valid() #不抛出异常
        serializer.is_valid(raise_exception=True)
        # 2.操作数据库
        serializer.save()
        # 3.返回响应
        return JsonResponse(data=serializer.data, status=201)

    def get(self, request):
        # 反序列化 验证完成 更新入库
        # 1.接收客户端提交的数据，获取pk值
        pk = 5
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return JsonResponse({'erroe': '此学生不存在'}, status=400)
        # 2.接收客户端的数据
        # 模拟客户端的数据
        data = {
            'name': 'sscxxx',
            'sex': False,
            'age': 25,
            'classmate': '303',
            'description': 'hehehe'
        }
        # 3.修改操作中的实例化序列化器对象
        serializer = Student2Serializer(instance=student, data=data)
        # 4.数据验证
        serializer.is_valid(raise_exception=True)
        # 5.入库
        serializer.save()
        # 3.返回响应
        return JsonResponse(data=serializer.data, status=201)


class StudentView(View):
    def get1(self, request):
        # 获取一个序列化对象
        # 1.获取数据集
        instance = Student.objects.first()
        # 2.实例化序列化器，得到序列化对象
        serializer = StudentSerializer(instance=instance)
        # 3.调用序列化对象的data属性方法获取转换后的数据
        data = serializer.data
        # 4.响应数据
        return JsonResponse(data=data, status=200, safe=False)

    def get2(self, request):
        # 获取多个序列化对象
        # 1.获取数据集
        student_list = Student.objects.all()
        # 2.实例化序列化器，得到序列化对象
        serializer = StudentSerializer(instance=student_list, many=True)
        # 3.调用序列化对象的data属性方法获取转换后的数据
        data = serializer.data
        # 4.响应数据
        return JsonResponse(data=data, status=200, safe=False)

    def get3(self, request):
        # 1.接收客户端提交的数据
        data = {
            'name': 'xxx',
            'sex': True,
            'age': 199,
            'classmate': '303',
            'description': 'hhhhhhhhh'
        }
        # 1.1实例化序列化器，获取序列化对象
        serializer = StudentSerializer(data=data)
        # 1.2调用序列化器进行数据验证
        # serializer.is_valid() #不抛出异常
        serializer.is_valid(raise_exception=True)
        # 1.3获取验证后的结果
        print(serializer.validated_data)
        # 2.操作数据库
        # 3.返回响应
        return JsonResponse(data=serializer.data, status=201)

    def get(self, request):
        # 验证完成，添加数据入库
        # 1.接收客户端提交的数据
        data = {
            'name': 'ssc1',
            'sex': True,
            'age': 27,
            'classmate': '301',
            'description': 'hahahahha'
        }
        # 1.1实例化序列化器，获取序列化对象
        serializer = StudentSerializer(data=data)
        # 1.2调用序列化器进行数据验证
        # serializer.is_valid() #不抛出异常
        serializer.is_valid(raise_exception=True)
        # 2.操作数据库
        serializer.save()
        # 3.返回响应
        return JsonResponse(data=serializer.data, status=201)

    def get6(self, request):
        # 反序列化 验证完成 更新入库
        # 1.接收客户端提交的数据，获取pk值
        pk = 5
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return JsonResponse({'erroe': '此学生不存在'}, status=400)
        # 2.接收客户端的数据
        # 模拟客户端的数据
        data = {
            'name': 'sscxxx',
            'sex': False,
            'age': 25,
            'classmate': '303',
            'description': 'hehehe'
        }
        # 3.修改操作中的实例化序列化器对象
        serializer = Student2Serializer(instance=student, data=data)
        # 4.数据验证
        serializer.is_valid(raise_exception=True)
        # 5.入库
        serializer.save()
        # 3.返回响应
        return JsonResponse(data=serializer.data, status=201)
