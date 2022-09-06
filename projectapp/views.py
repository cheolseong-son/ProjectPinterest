from lib2to3.pgen2.token import RPAR
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin


from projectapp.models import Project
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from projectapp.forms import ProjectCreationForm
# Create your views here.
from articleapp.models import Article
from subscriptionapp.models import Subscription
# from subscripbeapp.models import Subscription

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateVeiw(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk':self.object.pk})

class ProjectDetailView(DetailView, MultipleObjectMixin): 
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        # 유저가 현재 게시판의 구독정보를 가지고 있는지 확인
        project = self.object
        user = self.request.user

        if user.is_authenticated:
            # and function임
            subscription = Subscription.objects.filter(user=user, project=project)
        
        
        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list,
        subscription=subscription ,**kwargs)

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    
    paginate_by = 25
