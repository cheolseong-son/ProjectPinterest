from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord

@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
  # 요청받은 게시글로 redirect하기
  def get_redirect_url(self, *args, **kwargs):
    return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']})

  # 유저가 로그인 해야만 좋아요를 누를 수 있도록 함
  def get(self, *args, **kwargs):

    user = self.request.user
    article = get_object_or_404(Article, pk=kwargs['pk'])
    # 유저가 현 게시물에 좋아요를 눌렀는지 확인
    if LikeRecord.objects.filter(user=user, article=article).exists():
      messages.add_message(self.request, messages.ERROR, '"좋아요"는 한번만 가능합니다.')
      return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['pk']}))
    else:
      LikeRecord(user=user, article=article).save()
    # 좋아요 숫자 증가
    article.like += 1
    article.save()
    messages.add_message(self.request, messages.SUCCESS, '"좋아요"가 반영되었습니다.')
    return super(LikeArticleView, self).get(self.request, *args, **kwargs)
