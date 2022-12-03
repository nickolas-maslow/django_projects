from django.http import HttpResponse

errors = [
    'JobType matching query does not exist.',
    'Job matching query does not exist.',
]


def empty_request(exception):
    if str(exception) in errors:
        return HttpResponse('<h1>Empty request</h1>')
    else:
        return HttpResponse(f'{exception}')


