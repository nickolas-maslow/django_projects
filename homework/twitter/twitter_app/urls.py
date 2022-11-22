from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='startpage'),
    path('sign_up/', sign_up, name='sign_up'),
    path('data/', upload, name='upload')
]