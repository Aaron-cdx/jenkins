from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("hello welcome to the django! Try hard study to Jenkins!")
