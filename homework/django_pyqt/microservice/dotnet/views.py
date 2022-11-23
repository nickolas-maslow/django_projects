from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *


def index(request):
    if request.method == 'POST':
        if request.POST.get('login') == 'nick':
            with open('../logs.txt', 'w') as f:
                f.write(str(request))
            return HttpResponse('<h1 style="color: green; text-align: center;">Success!</h1>')
        else:
            return HttpResponse('<h1 style="color: red; text-align: center;">User not found.</h1>')
    return render(request, 'index.html')


def upload_json(request):
    client = {'name': 'nick', 'password': None}
    request_time = {'hour': 8, 'min': 24, 'sec': 12}
    customer = [client, request_time]
    return JsonResponse(customer, safe=False)


def todo(request):
    context = {'tasks': ToDoList.objects.all()}
    return render(request, 'todolist.html', context=context)
