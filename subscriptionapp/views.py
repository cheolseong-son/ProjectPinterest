
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView, ListView
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from articleapp.models import Article
from projectapp.models import Project
from subscriptionapp.models import Subscription


@method_decorator(login_required, 'get') # 로그인 여부 확인
class SubscriptionView(RedirectView):

    # 구독버튼을 눌렀을 경우 다시 해당 detail 페이지로 돌아가게 함
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    # 해당 pk의 프로젝트, 유저가 존재하고 Subscription 모델에 있으면 삭제 없는지 추가
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user

        subscription = Subscription.objects.filter(user=user, project=project)

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)

@method_decorator(login_required, 'get') # 로그인 여부 확인
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscriptionapp/list.html'
    paginate_by = 5

    # 특정 조건의 게시글만 가져오기
    def get_queryset(self):
        # 유저가 구독하고 있는 게시글 찾아오기
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=projects)
        
        return article_list


