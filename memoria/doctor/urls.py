from django.urls import path
from . import views


urlpatterns = [
    path('doctor/submit_patient_info/', views.submit_patient_info, name='submit_patient_info'),
    path('input/', views.input, name='input'),
    path('output/<str:patient_id>/', views.output, name='output')
]