from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    # return HttpResponse("hello welcome to the django! Try hard study to Jenkins!")
    # message = "Hello world~"
    message = "Hello world \n 本次是自动部署的，不含有任何的人工成分"
    message2 = "再增加一条测试记录"
    return render(request, "index.html", {"message": message, "message2": message2})
