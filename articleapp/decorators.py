# 데코레이터를 만듬 
from django.http import  HttpResponseForbidden
from articleapp.models import Article
from django.utils.decorators import method_decorator


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if not article.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated

