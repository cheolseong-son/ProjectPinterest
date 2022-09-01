
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect
from accountapp.models import HelloWorld

from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def hello_world(request):
    if request.method == "POST":
        # POST에서 "hello_world_input"이라는 이름의 값을 가져와라
        temp = request.POST.get('hello_world_input')
        # 데이터 저장
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})


# 계정
# reverse_lazy : class에서 사용, 
# reverse : 함수형에서 사용
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') # 로그인 성공시 갈 곳
    template_name = 'accountapp/create.html'

    