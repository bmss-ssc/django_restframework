from rest_framework.authentication import BaseAuthentication
from django.contrib.auth import get_user_model


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        user = request.query_params.get('user')
        # pwd = request.query_params.get('pwd')
        # if user != 'admin' or pwd != "admin":
        #     return None
        user = get_user_model().objects.filter(username=user).first()
        # print(user)
        return (user, None)
