from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets, mixins
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer


# 1.基于APIView编写5个API接口
class CourseAPIView(APIView):
    def get(self, request):
        # 1.从模型中获取所有信息
        queryset = Course.objects.all()
        # 2.序列化
        serializer = CourseSerializer(instance=queryset, many=True)
        # 3.返回结果
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # 1.接收客户端的数据
        data = request.data
        # 2.反序列化[验证保存数据]
        serializer = CourseSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 3.返回结果
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CourseInfoAPIView(APIView):
    def get(self, request, pk):
        try:
            instance = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(instance=instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            instance = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # 2.反序列化[验证保存数据]
        serializer = CourseSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        try:
            instance = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        instance.delete(status=status.HTTP_204_NO_CONTENT)

        return Response({})


# 2.基于GenericAPIView编写5个API接口
class CourseGenericAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseInfoGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# 3.基于GenericAPIView+Mixins编写5个API接口
class CourseMixinsGenericAPIView(mixins.ListModelMixin,
                                 mixins.CreateModelMixin,
                                 generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        # list 方法继承 ListModelMixin 而来
        return self.list(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # create 方法继承 CreateModelMixin 而来
        return self.create(self, request, *args, **kwargs)


class CourseInfoMixinsGenericAPIView(mixins.RetrieveModelMixin,
                                     mixins.UpdateModelMixin,
                                     mixins.DestroyModelMixin,
                                     generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)


# # 通用类视图集
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
