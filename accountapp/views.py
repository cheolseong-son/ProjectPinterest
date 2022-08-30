from hashlib import new
from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import HelloWorld

# Create your views here.
def hello_world(request):
    if request.method == "POST":
        # POST에서 "hello_world_input"이라는 이름의 값을 가져와라
        temp = request.POST.get('hello_world_input')
        # 데이터 저장
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return render(request, 'accountapp/hello_world.html', context={'hello_world_output':new_hello_world})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text':'GET METHOD!'})
