from django.urls import path
from . import views


urlpatterns = [
    path('in/', views.input, name='input'),
    path('out/', views.output, name='output')
]