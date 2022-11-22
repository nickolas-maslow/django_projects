from django.shortcuts import render


def index(request):
    context = {
        'upper': 'navbar',
        'lower': 'Base Info',
        'login': '',
    }
    return render(request, 'base.html', context=context)
