from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # 1 : 1 User 모델과 매칭
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 이미지는 media/profile 형태로 저장
    image = models.ImageField(upload_to = 'profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
