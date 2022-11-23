from django.urls import path
from .views import index


url_patterns = [
    path('', index)
]