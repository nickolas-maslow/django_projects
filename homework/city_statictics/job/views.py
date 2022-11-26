from django.shortcuts import render
from django.http import HttpResponse
from .models import Job


def index(request):
    context = {
        'job': Job.objects.all()
    }
    return render(request, 'index.html', context=context)
