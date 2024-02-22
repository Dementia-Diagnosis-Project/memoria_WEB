from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('input/', views.data_input_page, name='input'),
    path('output/', views.doctor, name='output'),
]