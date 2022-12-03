from django.shortcuts import render
from django.http import HttpResponse
from .models import Job, JobType
from .services import empty_request


def index(request):
    context = {
        'job': Job.objects.all()
    }
    return render(request, 'index.html', context=context)


def add_job(request):
    context = {
        'types': JobType.objects.all(),
    }
    if request.method == 'POST':
        try:
            name = request.POST['name']
            if name == '':
                return HttpResponse('Empty name!')
            description = request.POST['desc']
            job_type = request.POST.get("type")
            job_type_id = JobType.objects.get(type=job_type)
            job = job_type_id.pk
            Job.objects.create(name=name, description=description, type_of_job_id=job)
        except Exception as ex:
            return empty_request(ex)
    return render(request, 'add_job.html', context=context)


def delete_job(request):
    if request.method == 'POST':
        try:
            job = request.POST['job']
            Job.objects.get(name=job).delete()
        except Exception as ex:
            return empty_request(ex)
    return render(request, 'delete_job.html')


def update_job(request):
    context = {
        'types': JobType.objects.all(),
    }
    if request.method == 'POST':
        try:
            name = request.POST['name']
            description = request.POST['desc']
            if description == '':
                return empty_request(Exception)
            job_type = request.POST.get("type")
            job_type_id = JobType.objects.get(type=job_type)
            job = job_type_id.pk
            Job.objects.filter(name=name).update(description=description,
                                                 type_of_job=job)
        except Exception as ex:
            return empty_request(ex)

    return render(request, 'update_job.html', context=context)


def get_categories(request):
    context = {
        'categories': JobType.objects   .all()
    }
    JobType.objects.all().delete()
    if request.method == 'POST':
        delete_type = request.POST['delete_category']
        add_type = request.POST['add_category']
        if add_type:
            if len(add_type) > 3:
                JobType.objects.create(type=add_type)
        if delete_type:
            if len(add_type) > 3:
                JobType.objects.get(type=delete_type).delete()

    return render(request, 'add_or_delete_category.html', context=context)
