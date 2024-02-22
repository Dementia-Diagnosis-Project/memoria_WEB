from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('input/', views.data_input_page, name='input'),
    path('output/', views.doctor, name='output'),
]