from django.http import JsonResponse
from django.shortcuts import render
from .models import *


def index(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        if login == User.objects.get():
            pass
    return render(request, 'index.html')


def sign_up(request):
    return render(request, 'sign_up.html')


def upload(request):
    user = {
        'login': '123',
        'password': '123'
    }
    request_time = {
        'year': 2022,
        'month': 'november',
        'day': 'monday'
    }
    user_list = [user, request_time]
    return JsonResponse(user_list, safe=False)