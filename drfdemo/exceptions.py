from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from django.db import DataError


def custom_exception_handler(exc, context):
    response = drf_exception_handler(exc, context)
    if response is None:
        if isinstance(exc, ZeroDivisionError):
            response = Response({'msg': '0不能作为除数！'})
        if isinstance(exc, DataError):
            response = Response({'msg': '数据存储异常！'})

    return response
