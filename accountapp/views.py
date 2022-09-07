
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden
from accountapp.decorators import account_ownership_required
from accountapp.forms import accountUpdateForm

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from articleapp.models import Article
from .forms import accountUpdateForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import account_ownership_required

from django.views.generic.list import MultipleObjectMixin

has_ownership = [account_ownership_required, login_required]

# 계정
# reverse_lazy : class에서 사용, 
# reverse : 함수형에서 사용
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') # 로그인 성공시 갈 곳
    template_name = 'accountapp/create.html'


# DetailView
class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list,**kwargs)

# UpdataView
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')

class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = accountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world') # 로그인 성공시 갈 곳
    template_name = 'accountapp/update.html'
    
    # method_decorator로 아래의 것을 대체할 수 있다
    # ## 로그인 상태에서 update를 사용할 수 있게 하기 위해
    # # get 방식일 경우
    # def get(self, *args, **kwargs):
    #     # 로그인 한 상태이고 request를 보내는 유저와 get_object()한 유저가 같다면
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    
    # # 포스트 방식일 경우
    # def post(self, *args, **kwargs):
    #     # 로그인 한 상태이고 request를 보내는 유저와 get_object()한 유저가 같다면
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().post(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden() <-- 여기까지 코드

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accuntapp:login')
    template_name = 'accountapp/delete.html'

    ## 로그인 상태에서 delete를 사용할 수 있게 하기 위해
    # # get 방식일 경우
    # def get(self, *args, **kwargs):
    #     # 로그인 한 상태이고 request를 보내는 유저와 get_object()한 유저가 같다면
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    
    # # 포스트 방식일 경우
    # def post(self, *args, **kwargs):
    #     # 로그인 한 상태이고 request를 보내는 유저와 get_object()한 유저가 같다면
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().post(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()


