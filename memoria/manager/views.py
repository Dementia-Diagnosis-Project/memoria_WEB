from django.shortcuts import render, redirect


def doctor(request):
    data = {
        "id": '002_S_5018'
    }
    return render(request, 'manager/real_patient.html',{'data': data})

#1 인퍼런스 함수 선언,
def inference(request, image_png):
    #2 모델 로드 후 모델 사용하도록, instance화 시킴
    #3 instance화 시킨거에 이미지를 넣는다
    #4 3의 결과물을 data.dict에 집어 넣는다
    # data = {'result': ~(이미지는 경로를 저장)}

    return render(request, 'manager/real_patient.html')

def data_input_page(request):


    return render(request, 'manager/input.html' )



