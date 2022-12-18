from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('', views.index),
    path('export_products_xls/', views.export_products_xls, name='exports'),
]