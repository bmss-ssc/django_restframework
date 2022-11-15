from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from drfdemo.authentication import CustomAuthentication


class ExampleView(APIView):
    # authentication_classes = [CustomAuthentication,]

    def get(self, request):
        print(request.user)
        print(type(request.user))
        if request.user.id:
            print('通过认证')
        else:
            print('未通过认证')

        return Response({'msg': 'ok'})


class HomeAPIView(APIView):

    def get(self, request):
        print(request.user)
        print(type(request.user))
        if request.user.id:
            print('通过认证')
        else:
            print('未通过认证')

        return Response({'msg': 'ok'})


from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from drfdemo.permissions import IsXiaoMingPermission


class HomeInfoAPIView(APIView):
    # 内置权限
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # 自定义权限
    # permission_classes = [IsXiaoMingPermission]

    def get(self, request):
        return Response({'msg': 'ok'})

    def post(self, request):
        return Response({'msg': 'ok'})


from rest_framework.generics import RetrieveAPIView
from school.models import Student
from school.serializers import StudentModelSerializer2
from rest_framework.throttling import UserRateThrottle


class Home2InfoAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer2
    # permission_classes = [IsXiaoMingPermission]
    throttle_classes = [UserRateThrottle]


class Demo1APIView(APIView):
    # 自定义限流
    throttle_scope = 'member'

    def get(self, request):
        return Response({'msg': 'ok'})


class Demo2APIView(APIView):
    # 自定义限流
    throttle_scope = 'vip'

    def get(self, request):
        return Response({'msg': 'ok'})


class Demo3APIView(APIView):
    # 自定义限流
    throttle_scope = 'vvip'

    def get(self, request):
        return Response({'msg': 'ok'})


from rest_framework.generics import ListCreateAPIView
from stuapi.models import Student
from students.serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class StudentPageNumberPagination(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'size'
    page_size = 2
    max_page_size = 4


class Demo4APIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['sex', 'classmate']
    ordering_fields = ['id', 'age']
    # pagination_class = None
    # pagination_class = LimitOffsetPagination
    # pagination_class = PageNumberPagination
    pagination_class = StudentPageNumberPagination


class Demo5APIView(APIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        1/0
        return Response({'msg': 'ok'})
