from rest_framework.permissions import BasePermission


class IsXiaoMingPermission(BasePermission):
    # def has_permission(self, request, view):
    #     return bool(request.user and request.user.username == 'xiaoming')

    def has_object_permission(self, request, view, obj):
        from school.models import Student
        if isinstance(obj, Student):
            # 限制只有小明才能操作Student模型
            user = request.query_params.get('user')
            return user == 'xiaoming'

        else:
            return True
