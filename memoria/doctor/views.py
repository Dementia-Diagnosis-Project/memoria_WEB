from django.shortcuts import render, redirect
from .models import Patients, Diagnosis
from django.core.files.base import ContentFile
import base64

def submit_patient_info(request):
    if request.method == 'POST':
        # 환자 정보 수집
        patient_id = request.POST.get('id')
        name = request.POST.get('name')
        birth = request.POST.get('birth')
        gender = request.POST.get('gender')
        smoking = request.POST.get('smoking', False)
        drinking = request.POST.get('drinking', False)
        depression = request.POST.get('depression', False)
        specific = request.POST.get('specific', '')

        # 진단 정보 수집
        mmse = request.POST.get('mmseScore')
        hippo = request.POST.get('hippocampusVolume')
        mri_image = request.FILES.get('mri')

        # 필요한 경우, 데이터베이스에 정보 저장
        patient = Patients.objects.create(
            id=patient_id,
            name=name,
            birth=birth,
            gender=gender,
            smoking=smoking,
            drinking=drinking,
            depression=depression,
            specific=specific
        )

        diagnosis = Diagnosis.objects.create(
            id=patient_id,
            date='',
            mmse=mmse,
            hippo=hippo,
            mri=mri_image
        )

        return redirect('output', patient_id=diagnosis.id)
    else:
        # GET 요청 시 input.html로 리다이렉트
        return redirect('doctor/input.html')

def input(request):
    return render(request, 'doctor/input.html')

def output(request, patient_id):
    # 환자 정보 조회
    patient = Patients.objects.get(id=patient_id)
    # 진단 정보도 조회할 수 있습니다. 예: diagnosis = Diagnosis.objects.get(id=patient_id)

    context = {
        'patient': patient,
        # 'diagnosis': diagnosis, # 진단 정보가 있다면 함께 전달
    }
    return render(request, 'doctor/output.html', context)