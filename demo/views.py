from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from demo.serializers import StudentModelSerializer
from stuapi.models import Student


# APIView 基本视图类
class StudentAPIView(APIView):
    def get(self, request):
        # 1.从数据库中读取学生信息列表
        students = Student.objects.all()

        # 2.实例化序列化器，获取序列化对象
        serializer = StudentModelSerializer(instance=students, many=True)

        # 3.转换数据并返回给客户端
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # 1.获取客户端提交的数据，实例化序列化器，获取序列化对象
        serializer = StudentModelSerializer(data=request.data)

        # 2.反序列化[验证数据、保存到数据库]
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # 3.返回新增的模型数据给客户端
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class StudentInfoAPIView(APIView):
    def get(self, request, pk):
        # 1.获取模型对象
        try:
            instance = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(data={'error': '没有该同学'}, status=status.HTTP_404_NOT_FOUND)

        # 2.实例化序列化器，获取序列化对象
        serializer = StudentModelSerializer(instance=instance)

        # 3.转换数据并返回给客户端
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        # 1.获取模型对象
        try:
            instance = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(data={'error': '没有该同学'}, status=status.HTTP_404_NOT_FOUND)

        # 2.获取客户端提交的数据
        serializer = StudentModelSerializer(instance=instance, data=request.data)

        # 3.反序列化[验证数据、保存到数据库]
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # 4.返回新增的模型数据给客户端
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):

        try:
            Student.objects.get(pk=pk).delete()
        except Student.DoesNotExist:
            return Response(data={'error': '没有该同学'}, status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)


# Generic APIView 通用视图类
class StudentGenericAPIView(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request):
        # 1.从数据库中读取学生信息列表
        queryset = self.get_queryset()

        # 2.实例化序列化器，获取序列化对象
        serializer = self.get_serializer(instance=queryset, many=True)

        # 3.转换数据并返回给客户端
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # 1.获取客户端提交的数据，实例化序列化器，获取序列化对象
        serializer = self.get_serializer(data=request.data)

        # 2.反序列化[验证数据、保存到数据库]
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # 3.返回新增的模型数据给客户端
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class StudentInfoGenericAPIView(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, pk):
        # 1.获取模型对象
        instance = self.get_object()

        # 2.实例化序列化器，获取序列化对象
        serializer = self.get_serializer(instance=instance)

        # 3.转换数据并返回给客户端
        return Response(data=serializer.data)

    def put(self, request, pk):
        # 1.获取模型对象
        instance = self.get_object()

        # 2.获取客户端提交的数据
        serializer = self.get_serializer(instance=instance, data=request.data)

        # 4.反序列化[验证数据、保存到数据库]
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # 3.转换数据并返回给客户端
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        # 1.获取模型对象并删除
        self.get_object().delete()

        # 2.返回数据
        return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework.mixins import ListModelMixin, CreateModelMixin


class StudentMixinView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


class StudentInfoMixinView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)


from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    @action(methods=['get', 'post'], detail=False, url_path='user/login')
    def login(self, request):
        return Response({'msg': '登录成功！'})

    @action(methods=['get', 'post'], detail=True, url_path='user/login/log')
    def login(self, request, pk):
        # 用户登录历史记录
        print(self.action)
        return Response({'msg': '登录成功！'})
