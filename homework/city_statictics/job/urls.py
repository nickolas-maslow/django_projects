from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('add_job/', add_job, name='add_job'),
    path('delete_job/', delete_job, name='delete_job'),
]