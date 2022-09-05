
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    # on_delete = models.SET_NULL : 유저가 사라져도 게시글이 사라지지 않게 함
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article')
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to = 'article/',null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_created=True,null=True)
