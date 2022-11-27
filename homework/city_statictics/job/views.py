from django.shortcuts import render
from django.http import HttpResponse
from .models import Job


def index(request):
    context = {
        'job': Job.objects.all()
    }
    return render(request, 'index.html', context=context)


def add_job(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['desc']
        if 'Education' in request.POST['type']:
            type_of_job = 1
            Job.objects.create(name=name, description=description,
                               type_of_job_id=type_of_job)
        if 'MIA' in request.POST['type']:
            type_of_job = 2
            Job.objects.create(name=name, description=description,
                               type_of_job_id=type_of_job)
        if 'Legal proceedings' in request.POST['type']:
            type_of_job = 3
            Job.objects.create(name=name, description=description,
                               type_of_job_id=type_of_job)
    return render(request, 'add_job.html')


def delete_job(request):
    if request.method == 'POST':
        job = request.POST['job']
        Job.objects.get(name=job).delete()
    return render(request, 'delete_job.html')