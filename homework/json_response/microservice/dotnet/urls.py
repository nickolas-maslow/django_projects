from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('data/', upload_json),
    path('todo/', todo),
]
