from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('dotnet.urls')),
    path('admin/', admin.site.urls),
]
