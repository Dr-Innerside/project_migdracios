from django.http import HttpResponse

def base_response(request):
    return HttpResponse("가장 처음에 하는 테스트 리턴")
