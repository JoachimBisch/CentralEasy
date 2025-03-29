from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('detail/<str:service_title>/', views.detail, name='detail')
]
