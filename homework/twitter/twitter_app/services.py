from .models import User
from django.http import HttpResponse


def add_user(user_login, user_password, check_user_password):
    if user_login <= 3:
        if user_password == check_user_password:
            return User.objects.create(login=user_login, password=user_password)
        else:
            return HttpResponse('Passwords are not the same!')
    else:
        return HttpResponse('Login must be 4 letters at least!')
