from django.shortcuts import render


def homepage(request):
    context = {'title': 'homepage'}
    return render(request, 'base.html', context=context)

