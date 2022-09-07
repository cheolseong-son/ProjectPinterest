from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class LikeRecord(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_record')
  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like_record')
  # 유저가 기사에 좋아요를 눌렀다는 것은 유일해야 한다.
  class Meta:
    unique_together = ['user', 'article']