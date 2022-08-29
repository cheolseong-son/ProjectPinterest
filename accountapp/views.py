from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return HttpResponse("hello world!, 안녕하세요")
